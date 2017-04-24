#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
进程间共享数据

通过value\array共享数字和列表数据
'''

from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    print num.value
    print arr[:]

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print num.value
    print arr[:]
