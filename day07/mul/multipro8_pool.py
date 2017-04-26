#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
进程池

'''

from multiprocessing import Process,Pool
import time

def f(x):
    #print x*x
    time.sleep(1)
    return x*x
if __name__ == '__main__':
    pool = Pool(processes=5)   #并行5个进程
    res_list = []

    for i in range(10):
        res = pool.apply_async(f,[i,])   #pool.apply_async异步执行      pool.apply同步执行即串行
        res_list.append(res)             #将进程的结果追加到一个列表中    注意这里的列表中的元素实际上都是一个实例

    for r in res_list:                   #由于列表元素是进程实例因此需要使用如下方式遍历
        print r.get()
