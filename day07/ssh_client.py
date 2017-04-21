#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
使用paramiko模块远程管理服务器
通过密码管理
'''

import paramiko

ssh = paramiko.SSHClient()      #实例化一个客户端
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #自动恢复yes，在我们使用ssh客户端链接的时候第一次的时候都会让我们输入一个yes确定的
ssh.connect('192.168.75.133', 22, 'root', '123456')
stdin,stdout,stderr = ssh.exec_command('du *')     #定义三个变量进行输出，默认输出是个元组会赋值给三个变量
print stdout.read()
ssh.close()