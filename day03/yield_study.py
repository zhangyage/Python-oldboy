#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
生成器函数
'''
def foo():
    yield 1
    yield 2
    yield 3
    
re = foo()
print re          #返回的是一个生成器

for i in re:      #循环输出
    print i