#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
t1.join(timeout)  #设置子线程等待主线程的时间
t1.join()         #join是设置等待时间   如果子线程没有完成就一直等待
t1.join(5)        #设置5是等待子线程5秒，5秒后不再等待继续主线程
'''

from threading import Thread


def Foo(arg):
    print arg

print 'before'    
t1 = Thread(target=Foo,args=(1,))  #创建线程的固定格式
t1.start()   #执行线程
t1.join(5)   #join是设置等待时间   如果子线程没有完成就一直等待   设置5是等待子线程5秒，5秒后不再等待继续主线程

print 'after'