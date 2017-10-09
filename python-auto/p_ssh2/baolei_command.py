#!/usr/bin/env python
# -*- coding:utf-8 -*-
#通过堡垒机跳转时间命令传输

import paramiko
import os
import sys
import time


blip = "121.42.191.190"    #定义的堡垒机信息
bluser = "zhangyage"
blpasswd = "MCya9B7ewPoTeNT8"

hostname = "116.196.69.47" #定义的业务主机信息
username = "root"
password = "Zhangyage"

port = 22
passinfo = '\'s password: ' #输入服务器密码的前标识串
paramiko.util.log_to_file('syslogin')  #发送paramiko日志到syslogin中

ssh = paramiko.SSHClient()             #ssh登录堡垒机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip, port=22, username=bluser, password=blpasswd)  #创建ssh链接


channel = ssh.invoke_shell()  #创建新的会话，开启命令调用
channel.settimeout(10)        #会话命令执行超时时间，单位为秒

buff = ''
resp = ''
channel.send('ssh ' +username+'@'+hostname+'\n')    #发送ssh链接命令
while not buff.endswith(passinfo):                  #ssh登录信息判断，
    try:
        resp = channel.recv(9999)
        print resp
    except Exception,e:
        print 'Error info:%s connection time' % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff +=resp
    if not buff.find('yes/no') ==-1:                #输出串含有“yes/no”发送yes并回车
        channel.send('yes\n')
        buff=''

channel.send(password+'\n')         #发送业务主机密码

buff = ''
while not buff.endswith('# '):     #输出串是#号表明校验已经通过，退出while
     resp = channel.recv(9999)
     if not resp.find(passinfo) ==-1:  #输出串含有password说明密码错误
        print 'Error info:Autentical failed.'
        channel.close()               #关闭链接对象后退出
        ssh.close()
        sys.exit()
     buff += resp
    
    
channel.send('ifconfig\n')        #认证通过后发送ufconfig命令查看结果
buff = ''
try:
    while buff.find('# ') == -1:
        resp = channel.recv(9999)
        buff += resp
except Exception,e:
    print "error info:" +str(e)
    
print buff                 #打印输出结果
channel.close()
ssh.close()