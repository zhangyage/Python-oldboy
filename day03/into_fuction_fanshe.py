#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
hostname  内存
主机A      8*8
主机B      
'''

a = '8*8'
b = '8+8'
print eval(a)
print eval(b)

#反射
#通过字符串的方式导入sys模块
temp = 'sys'
model = __import__(temp)
print model.path

#如果我们把模块和函数都使用字符串的话可以使用如下方式
temp = 'sys'
func = 'path'
model = __import__(temp)
Function = getattr(model, func)     #使用getattr执行函数
print Function