#!/usr/bin/env python
# -*- coding:utf-8 -*-

import paramiko
from sys import stdout, stderr

hostname = "116.196.69.47"
username = "root"
password = "Zhangyage"

paramiko.util.log_to_file('syslogin')  #发送paramiko日志到syslogin中
ssh = paramiko.SSHClient()             #创建ssh链接对象
##ssh.load_system_host_keys()            #获取客户端的host_keys
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=hostname, port=22, username=username, password=password)  #创建ssh链接
stdin,stdout,stderr =ssh.exec_command('free -m')  #调用远程执行命令的方法
print stdout.read()
ssh.close()