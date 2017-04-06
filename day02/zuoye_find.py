#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
编写一个程序当你输入字符串的时候输出文件中存在字符串对应的行
'''

print "欢迎使用员工信息查询系统"

chazhao = raw_input("please input your find zifuchuan:")

f1 = file('passwd','wb')
for i in f1.readlines():
    if chazhao in i:
        #print  i.replace(chazhao,\033[41;33mchazhao\033[0m)
        print i,
    else:
        continue
    
f1.close()
