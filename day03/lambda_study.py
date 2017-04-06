#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
内置函数练习
help()   dir()  vars() type() id() 
三元方程练习
'''

temp = None
if 1>3:
    temp = 'gt'
else:
    temp = 'lt'
print temp


result = 'gt' if 1>3 else 'lt'
print result


#内置函数lambda
tmp = lambda x,y:x+y
print tmp(4,10)

##
def foo(x,y):
    print x+y
foo(4,5)  


l = [x*2 for x in range(10)]
print l

#内置函数map
print map(lambda x:x*2,range(10))  


