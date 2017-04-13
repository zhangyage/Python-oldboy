#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
模仿socket的客户端
   和client.py配合使用
'''

import socket

sk = socket.socket()       #创建socket类的实例

ip_port = ('127.0.0.1',9000)
sk.bind(ip_port)           #绑定地址和端口
sk.listen(5)
#上面是服务端的绑定设置

while True:
    conn,address = sk.accept()       #等待客户端连接
    conn.send('Hello,client')
    flag = True
    while flag:
        data = conn.recv(1024)
        print data
        if data == 'exit':
            flag = False
        conn.send('sb')
    conn.close()

