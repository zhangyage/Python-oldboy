#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
进程间的通讯

通过Queue共享进程数据
'''

from multiprocessing import Process,Queue


def run(q,n):
    q.put([n,'multiprocessing'])

    
if __name__ =='__main__': 
    q=Queue()
    q.put('one')
    for i in range(5):
        p = Process(target=run,args=[q,i])
        p.start()
    while True:
        print q.get()   
