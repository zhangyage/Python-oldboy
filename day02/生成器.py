#!/usr/bin/env python
# -*- coding:utf-8 -*-

#列表生成器
a = [i+1 for i in range(10)]
print a

a= [i if i<5 else i*i for i in range(10)]
print a

a2 = (i for i in range(1000))
print a2    #<generator object <genexpr> at 0x00000000055FE360>  这个时候a2就是生成器

print next(a2)   #0   使用next()去除数据
print next(a2)   #1




def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print 'before yield'
        yield b       #把函数的执行过程冻结在这一步，并且把b的值返回给外面的next()      generator
        print b
        a,b = b,a+b
        n = n+1
    return 

f = fib(15)

next(f)
next(f)
next(f)
next(f)
