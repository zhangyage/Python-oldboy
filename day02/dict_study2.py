#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
字典学习
'''
dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

#循环遍历所有的key
for i in dic:
    print i

#循环遍历所有的value
for i in dic:
    print dic[i]
    
#循环遍历所有的key,value
for i in dic:
    print i,dic[i]
print '--------------'    

#在字典中添加一个新的建值  k4,v4
dic.update(k4='v4')
print dic

#删除字典中的k5存在就删除，不存在就返回None
if dic.has_key('k5'):
    dic.pop('k5')
else:
    print None
    
#获取字典中k2的值
print dic['k2']

#获取字典中的k6的值，不存在就返回None
if dic.has_key('k5'):
    dic['k6']
else:
    print None
    
#现有dic2={'k1':'v111','a':'b'}通过一行操作使dic2={'a': 'b', 'k3': 'v3', 'k1': 'v1', 'k2': 'v2', 'k4': 'v4'}
dic2={'k1':'v111','a':'b'}
print dict( dic2, **dic )
#dict( dic2, **dic )   合并两个字典，相同的key时以**dic为准

lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
#使用两种方法将列表中的‘tt’变化为大写的
#lis[0][1][2]['k1'][0] = 'TT'
lis[0][1][2]['k1'][0]=lis[0][1][2]['k1'][0].upper()
print lis

