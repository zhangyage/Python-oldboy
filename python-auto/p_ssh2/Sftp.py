#!/usr/bin/env python
# -*- coding:utf-8 -*-
#SFTPClient() 类实现文件操作

import paramiko
from paramiko import sftp

hostname = "116.196.69.47"
username = "root"
password = "Zhangyage"
port = 22

try:
    t = paramiko.Transport((hostname,port)) 
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    
    sftp.put("D:/\workspace/\Python-oldboy/\python-auto/\diff.py","/root/test")  #上传文件
    sftp.get("/root/scan.py","test.py")  #下载文件
    sftp.mkdir("/root/SFTPT",0755)   #创建目录
    sftp.rmdir("/root/test1")        #删除目录
    sftp.rename("/root/test.sh","/root/kankan.sh")   #文件重命名
    print sftp.stat("/root/kankan.sh")    #打印文件信息
    print sftp.listdir("/root/source")    #打印目录列表
    t.close()
except Exception,e:
    print str(e)
    