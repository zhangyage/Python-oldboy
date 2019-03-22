#!/usr/bin/env python
# -*- coding:utf-8 -*-

eat = 23+45+67
cloth = 34+89+79

print type(eat) 

print ('total', eat + cloth)

n = ['old_driver','rain','shanshan','peiqi','black_gril']
n.insert(-1,'alex')
print n

n[2] = '姗姗'
print n

print n.index('peiqi')
for i in range(len(n)):
    print i , n[i]
    
for i in enumerate(n):
    print i
    
for i in range(len(n)):
    if i%2 == 0:
        n[i] =-1
    print i , n[i]
    
names = [1,2,3,4,5,2,7,2,8,9,2]
print names.count(2)
print names.index(2)
print  names.index(2) + names[names.index(2)+1:].index(2) + 1
#        第一个的位置               截断

print hash('123')
a='123'
print hash(a) 

import sys
sys.getrecursionlimit()
sys.setrecursionlimit(n)
sys.getdefaultencoding()
sys.getfilesystemencoding()
    