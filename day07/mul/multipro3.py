#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
进程间的通讯

当我们使用进程和线程的时候，我们会发现使用线程的时候列表是可传递数值的，是空享内存的

但是我们使用进程的时候会发现进程数据是不共享的列表每次都是一个元素输出
'''

from multiprocessing import Process
from threading import Thread


def run(info_list,n):
    info_list.append(n)
    print info_list

'''    
if __name__ =='__main__':    
    info = []
    for i in range(10):
        p = Process(target=run,args=[info,i])
        p.start()
'''
    
if __name__ =='__main__':    
    info = []
    for i in range(10):
        t = Thread(target=run,args=[info,i])
        t.start()
