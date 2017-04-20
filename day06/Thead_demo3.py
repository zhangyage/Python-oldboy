#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
自己模仿线程创建一个线程类
线程start的时候使用的run方法，我们也创建一个
'''

from threading import Thread
import time

class MyThread(Thread):  #继承系统的线程类
    
    def run(self):
        #time.sleep(10)
        print '我是线程！'
        Thread.run(self)        #调用父类的run方法
        

def Bar():
    print 'Bar'
    
t1 = MyThread(target=Bar)  #没有参数的传递可以不写arg
t1.start()
print 'over'



