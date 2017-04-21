#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
使用paramiko模块远程管理服务器
通过key登录 
'''

import paramiko

private_key_path = 'D:\workspace\Python-oldboy\day07\zhangyage_pass'
#key = paramiko.RSAKey.from_private_key_file(filename, password)
key = paramiko.RSAKey.from_private_key_file(private_key_path,'12345678')  #private_key_path是秘钥文件的位置，'12345678'是秘钥的口令

ssh = paramiko.SSHClient()      #实例化一个客户端
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   #自动恢复yes，在我们使用ssh客户端链接的时候第一次的时候都会让我们输入一个yes确定的
ssh.connect('192.168.75.133', 22, username='root', pkey=key)
stdin,stdout,stderr = ssh.exec_command('ifconfig')     #定义三个变量进行输出，默认输出是个元组会赋值给三个变量
print stdout.read()
ssh.close()