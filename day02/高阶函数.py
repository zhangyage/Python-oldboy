#!/usr/bin/env python
# -*- coding:utf-8 -*-

#高阶函数练习
#函数的参数可以接收一个变量，那么函数也是可以接收一个函数作为参数的，这种函数被叫做高阶函数
def func(x,y):
    return x+y

def calc(x):
    return x


print calc(func)


#import sys
#print sys.getrecursionlimit()