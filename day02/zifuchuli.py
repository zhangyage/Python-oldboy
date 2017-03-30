#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
字符处理的方法
'''

msg = "what's Your company's name?"

print msg.find('name')       #查找对应单词的位置 
print msg.capitalize()       #首字母大写
print msg.upper()            #全部转换为大写
print msg.upper().lower()    #lower()全部转换为小写
print msg.swapcase()         #大小写互换

print msg.split()            #将字符串转换为列表，默认使用空格分割
print msg.split("'")         #使用'好作为分割符分割字符串

print "|".join(msg.split())  #使用|号作为连接符连接列表
print len(msg)               #输出字符串的长度
print msg.startswith('wh')   #以什么开头
print msg.replace('o', 'A')  #替换，将字符串中的o替换为A