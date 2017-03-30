#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
练习文件读写
'''

f1 = file('passwd','r')
for line in f1.readlines():
    #print line         #print默认输入有换行
    #print line,        #line,连续输出去除换行符
    print line.strip('\n').split(':')
    #strip去除换行符，split是以：符号分割
f1.close()

f1.tell()
#可以输出你在文件的什么位置
f1.seek(0)
#直接指针到文件开头