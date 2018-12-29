#!/usr/bin/env python
# -*- coding:utf-8 -*-


def calc(x,y):
    if x< y:
        return x*y
    else:
        return x/y
    
print calc(10, 5)

#上面的函数可以使用匿名函数转换
func = lambda x,y: x*y if x< y else x/y
print(func(10,5))