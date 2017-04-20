#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time


num = 0

def run(n):
    time.sleep(1)
    
    global num
    lock.acquire()     #获取锁
    num +=1
    print '%s\n' %num
    lock.release()     #释放锁
    
lock = threading.Lock()   #实例化锁
    
for i in range(100):
    t = threading.Thread(target=run,args=(i,))
    t.start()

'''
    总结：使用如上线程你会发现问题，并没有输出到100会出现数据丢失的问题
'''