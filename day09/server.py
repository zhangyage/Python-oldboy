#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type:text/html\r\n\r\n")
    client.send("<a href='http://www.baidu.com'>hello,zhang</a>")
    
    
    
def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip_port = ('localhost',8080)
    sock.bind(ip_port)
    sock.listen(5)
    
    while True:
        connection,address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()