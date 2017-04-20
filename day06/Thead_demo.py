#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
t1 = Thread(target=Foo,args=(1,))  #创建线程的固定格式
target=Foo指定要执行的函数    args传递参数，多个参数用,隔开

t1.start()   #执行线程
'''

from threading import Thread


def Foo(arg):
    print arg

print 'before'    
t1 = Thread(target=Foo,args=(1,))  #创建线程的固定格式
t1.setDaemon(True)   #对应的是可以改变isDaemon()的值   确定是否是守护线程   这个设置一定要在start之前设置
t1.start()   #执行线程
print t1.isDaemon()   #默认情况下是False   意思是主线程不等待子线程
print t1.getName()  #得到线程的名字
print 'after'