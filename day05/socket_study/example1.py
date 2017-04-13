#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
socket练习
'''

import socket

def handle_request(client):
    buf = client.recv(1024)                #服务端接收收据
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("Hello,World!")

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',8080))
    sock.listen(5)
    
    while True:
        connection,address = sock.accept()   #connection代表客户端,address代表客户端的地址
        handle_request(connection)
        connection.close()

if __name__ == "__main__":
    main()