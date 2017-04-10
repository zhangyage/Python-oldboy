#!/usr/bin/env python
# -*- coding:utf-8 -*-
#from reflect.backend import account


#实例二   传输URl返回不同的结果
data = raw_input('请输入地址:')
#url格式  account/login

'''
#没有使用反射的调用方法
if data == 'account/login':
    account.login()
elif data == 'account/logout':
    account.logout()
'''
arry = data.split('/')
userspance = __import__('backend.'+arry[0])
model = getattr(userspance, arry[0])
func = getattr(model, arry[1]) 
func()
    