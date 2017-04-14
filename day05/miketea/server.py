#!/usr/bin/env python
# -*- coding:utf-8 -*-

import SocketServer
import json
import time
from models.model import UserInfo,ChatRecord

class MyServer(SocketServer.BaseRequestHandler):
    def setup(self):
        pass
    
    def handle(self):
        
        container = {'key':'','data':''}
        container['data'] = 'OK...'
        
        conn = self.request
        conn.sendall(json.dumps(container))
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