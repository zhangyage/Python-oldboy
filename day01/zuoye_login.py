#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
输入用户名密码
认证成功后显示欢迎信息
输错三次后锁定
使用时需要先创建文件lock.txt
'''
import os
if not os.path.exists('lock.txt'):
    f = file('lock.txt','w')
    f.close()

for i in range(3):
    username = raw_input('login:')
    password = raw_input('password:')
    f1 = file('lock.txt')
    list1 = []
    while True:
        line = f1.readline()            
        if len(line) == 0:
            break
        list1.append(line) 
    f1.close() 
    if username in list1:
        print ("用户名为：{0}的账号已经被锁定了！".format(username))
        break
    elif username == 'zhangyage' and password == '123456':
        print'''username:%s    
--------------------------
|    login successful!   |
--------------------------
''' % (username)
        break
    else:
        print("账号密码错误！请再次输入！您还有{0}次机会".format(2-i))
else:
    f = file('lock.txt','ab')
    f.write(username)
    f.close()
        