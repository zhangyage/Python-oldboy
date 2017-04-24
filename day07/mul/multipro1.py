#!/usr/bin/env python
# -*- coding:utf-8 -*-


from multiprocessing import Pool
import time

'''
演示单进程和多进程的区别
主要体现在执行时间上
'''
#单进程
def f(n):
    time.sleep(0.1)
    return n*n

#print map(f,range(10))
    

#多进程
if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, range(10)))

