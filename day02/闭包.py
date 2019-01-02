#!/usr/bin/env python
# -*- coding:utf-8 -*-

#闭包   在外部执行内部函数，并且在外部可以返回内部函数使用的使用的值和变量

def func():
    n = 10
    def func2():
        print ("func2",n)
    return func2

f = func()
print (f)
f()
