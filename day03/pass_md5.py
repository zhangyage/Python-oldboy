#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
MD5加密
MD5是不能反向解析的，同样的字符每次加密都是一样的值
'''
import hashlib

hash = hashlib.md5()    #实例化对象创建一个MD5对象
hash.update('admin')    #加密
print hash.hexdigest()

#print hash.digest()