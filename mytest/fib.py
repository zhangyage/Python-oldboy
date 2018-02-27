#!/usr/bin/env python
# -*- coding:utf-8 -*-

def fib(n):
    '''
        斐波那契数列练习求和  练习的是递归
    '''
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
if __name__ == "__main__":
    f = fib(10)
    print f