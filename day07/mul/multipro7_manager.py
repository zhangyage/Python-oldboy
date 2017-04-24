#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
进程间共享数据

通过Manager()共享数字和列表数据   在日常使用更多
'''

from multiprocessing import Process, Manager

def f(d,l):
    d[1] = '1'
    d['name'] = 'zhangyage'
    l.reverse()


if __name__ == '__main__':
    manager = Manager()
    
    d=manager.dict()
    l=manager.list(range(10))
    #print type(d)
    #print type(l)
    
    p = Process(target=f,args=(d,l))
    p.start()
    p.join()
    
    print d
    print l
