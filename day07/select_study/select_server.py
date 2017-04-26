#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
select异步练习   服务端
'''

import select
import socket
import sys
import Queue


#create a TCP/ip socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)     #让后面等待的socket链接暂时排队

#bind the socket to the port
server_address = ('localhost',10000)
print >>sys.stderr,'starting up on %s port %s' % server_address
server.bind(server_address)

#最大链接数设置
server.listen(5)

#建立列表一个是接受的一个是发送的
# Sockets from which we expect to read     所有进来的链接(包括新进来的链接和已经建立的链接)
inputs = [ server ]

# Sockets to which we expect to write      所有输出的链接
outputs = [ ]

# Outgoing message queues (socket:Queue)
message_queues = {}

while inputs:

    # Wait for at least one of the sockets to be ready for processing
    print >>sys.stderr, '\nwaiting for the next event'
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    #handle  inputs
    for s in readable:
        
        if s is server: #如果是server代表有新的客户端链接过来，代表一个先的实例（处理新连接）
        # A "readable" server socket is ready to accept a connection 
            connection, client_address = s.accept()
            print >>sys.stderr,'new connection from',client_address
            connection.setblocking(0) 
            inputs.append(connection)
           
            # Give the connection a queue for data we want to send 
            message_queues[connection] = Queue.Queue() 
            
        else:   #处理老链接   处理数据
            data = s.recv(1024)
            if data:
            # A readable client socket has data 
                print >>sys.stderr,'receved "%s" from %s' %(data, s.getpeername()) 
                message_queues[s].put(data)
                # Add output channel for response 
                if s not in outputs: 
                    outputs.append(s) 
            else: 
                # Interpret empty result as closed connection 
                print >>sys.stderr, 'closing', client_address, 'after reading no data'
                # Stop listening for input on the connection 
                if s in outputs: 
                    outputs.remove(s)  #既然客户端都断开了，我就不用再给它返回数据了，所以这时候如果这个客户端的连接对象还在outputs列表中，就把它删掉 
                inputs.remove(s)    #inputs中也删除掉 
                s.close()           #把这个连接关闭掉 
 
                # Remove message queue 
                del message_queues[s] 
    # Handle outputs 
    for s in writable: 
        try: 
            next_msg = message_queues[s].get_nowait() 
        except Queue.Empty: 
            # No messages waiting so stop checking for writability. 
            print >>sys.stderr, 'output queue for', s.getpeername(), 'is empty'
            outputs.remove(s) 
        else: 
            print >>sys.stderr, 'sending "%s" to %s' % (next_msg, s.getpeername()) 
            s.send(next_msg) 
            
    
    # Handle "exceptional conditions" 
    for s in exceptional: 
        print >>sys.stderr, 'handling exceptional condition for', s.getpeername() 
        # Stop listening for input on the connection 
        inputs.remove(s) 
        if s in outputs: 
            outputs.remove(s) 
        s.close() 
     
        # Remove message queue 
        del message_queues[s] 




        
            