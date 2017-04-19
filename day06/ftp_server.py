#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
G:/temp   目录要提前创建一下，做为ftp的根目录
'''

import SocketServer
import os


class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        base_path = 'G:/temp'
        conn = self.request
        print 'connected...'
        while True:
            pre_data = conn.recv(1024)
            #获取请求的方法、文件名、文件大小
            
            cmd,file_name,file_size=pre_data.split('|')
            #已经接受的文件大小
            recv_size = 0
            #上传文件路径拼接
            file_dir = os.path.join(base_path,file_name)
            
            f = file(file_dir,'wb')
            Flag = True
            while Flag:
                #未上传完成
                if int(file_size) > recv_size:
                    #最多接收1024，可能接收的小于1024
                    data = conn.recv(1024)
                    recv_size+=len(data)
                #上传完毕退出循环
                else:
                    recv_size = 0
                    Flag = False
                    continue
                f.write(data)
            print 'upload successed.'
            f.close()

instance = SocketServer.ThreadingTCPServer(('127.0.0.1',9000),MyServer)
instance.serve_forever()
            
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                