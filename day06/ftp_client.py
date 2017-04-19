#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
    #cmd:put get 是执行的命令   path:是路径
    file_name  获取文件名
    file_size  获取文件大小
    
    目前客户端端支持上传
'''
import socket
import os

ip_port =('127.0.0.1',9000)
sk = socket.socket()
sk.connect(ip_port)

while True:
    input = raw_input('path:')
    cmd,path = input.split('|')                #cmd:put get 是执行的命令   path:是路径
    
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    
    sk.send(cmd+"|"+file_name+'|'+str(file_size))
    send_size = 0
    f = file(path,'rb')
    Flag = True
    
    while Flag:
        if send_size + 1024 > file_size:
            data = f.read(file_size-send_size)
            Flag = False
        else: 
            data = f.read(1024)
            send_size+=1024
        sk.send(data)
        f.close()
sk.close()
            
            
            
            
            