#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
普通用户密钥登录  切换到root
'''


import paramiko
import time

def verification_ssh(host,username,port,root_pwd,cmd):
    private_key_path = 'D:\workspace\Python-oldboy\my_study\id_rsa'
    #key = paramiko.RSAKey.from_private_key_file(filename, password)
    key = paramiko.RSAKey.from_private_key_file(private_key_path,'5A5v7dzUnJB')  #private_key_path是秘钥文件的位置，'12345678'是秘钥的口令
    s=paramiko.SSHClient() 
    #s.load_system_host_keys() 
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname = host,port=int(port),username=username,pkey=key)
    if username != 'root':
        ssh = s.invoke_shell()
        time.sleep(0.1)
        ssh.send('su - \n')
        buff = ''
        while not buff.endswith('Password: '):
            resp = ssh.recv(9999)
            buff +=resp
        ssh.send(root_pwd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999)
            buff +=resp
        ssh.send(cmd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999)
            buff +=resp
        s.close()
        result = buff
    else:
        stdin, stdout, stderr = s.exec_command(cmd)
        result = stdout.read()
        s.close()
    return result

print verification_ssh(host='118.190.137.83',username='meifajiazu',port=22,root_pwd='Zuimeifang2017',cmd='cd /home/tomcat && ls -l')