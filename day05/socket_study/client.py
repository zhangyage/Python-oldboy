#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
模仿socket的客户端，
   和server.py配合使用
'''

import socket

client = socket.socket()

ip_port = ('127.0.0.1',9000)
client.connect(ip_port)
while True:
    data = client.recv(1024)     #接收服务端的数据
    print data
    inp = raw_input('client:')
    client.send(inp)             #发送消息到服务端
    if inp == 'exit':
        break
