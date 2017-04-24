#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
进程同步

通过lock同步进程的数据
'''

from multiprocessing import Process,Lock


def run(l,n):
    l.acquire()
    print 'lock',n
    l.release()
    
if __name__ =='__main__': 
    lock = Lock()
    
    for num in range(10):
        p = Process(target=run,args=(lock,num))
        p.start()
