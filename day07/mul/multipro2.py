#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
验证父子进程关系
'''


from multiprocessing import Pool
from multiprocessing import Process
import os
import time

def info(title):
    print title
    print 'module name',__name__
    if hasattr(os, 'getppid'):
        print 'parent process:',os.getppid()
    time.sleep(15)
    print 'procson id:',os.getpid()
    
def f(name):
    info('function f')
    print 'hello',name
    
if __name__ == '__main__':
    info('main line')
    print '---------------------------'
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
    
        
