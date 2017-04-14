#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
多线程
'''
import SocketServer

class MyServer(SocketServer.BaseRequestHandler):
    
    def handle(self):
        #print self.request
        #print self.client_address
        #print self.server
        conn = self.request
        conn.send('Hello,client')
        flag = True
        while flag:
            data = conn.recv(1024)
            print data
            if data == 'exit':
                flag = False
        
            conn.send('sb')
        conn.close()
        
if __name__ == "__main__":
    server = SocketServer.ThreadingTCPServer(('127.0.0.1',9000),MyServer)
    server.serve_forever()