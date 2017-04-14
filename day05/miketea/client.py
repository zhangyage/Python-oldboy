#!/usr/bin/env python
# -*- coding:utf-8 -*-


import socket
import sys
import json

ip_port =('127.0.0.1',9000)
sk = socket.socket()
sk.connect(ip_port)

container = {'key':'','data':''}
while True:
    data = sk.recv(1024)
    rev_data = json.loads(data)
    print rev_data['data']
    if not rev_data['key']:
        user = raw_input('username:')
        pwd = raw_input('password:')
        rev_data['data']=[user,pwd]
        sk.sendall(json.dumps(rev_data))
    else:
        inp = raw_input('reply')
        rev_data['data'] = inp 
        sk.sendall(json.dumps(rev_data))
        if inp == 'exit':
            break