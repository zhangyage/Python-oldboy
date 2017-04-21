#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
信号量学习

应用场景mysql最大链接数应用
'''

import threading
import time


num = 0


def run(n):
    time.sleep(1)
    
    global num
    samp.acquire()     #获取锁
    time.sleep(1)
    num +=1
    print '%s\n' %num,
    samp.release()     #释放锁
    
#lock = threading.RLock()   #实例化锁
samp = threading.BoundedSemaphore(4)  #同时可以执行多少个线程
    
for i in range(100):
    t = threading.Thread(target=run,args=(i,))
    t.start()

