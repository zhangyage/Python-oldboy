#!/usr/bin/env python
# -*- coding:utf-8 -*-


data = list(range(10))
print data

def f2(n):
    return n*n

#使用map函数，输出0-9的平方结果， map需要两个参数，一个是对应的函数，这个也可以使用匿名函数代替，另一个参数就是一个列表作为参数传递给前面的函数
print map(f2,data)

#同样也可以这样些
print map(lambda x:x*x, data)
