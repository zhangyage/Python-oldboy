#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time


num = 0
num2 = 0 

def run(n):
    time.sleep(1)
    
    global num
    global num2
    lock.acquire()     #获取锁
    num +=1
    
    lock.acquire()     #获取锁
    num2 +=2
    print '%s\n' %num
    lock.release()     #释放锁
    lock.release()     #释放锁
    
lock = threading.RLock()   #实例化锁
    
for i in range(100):
    t = threading.Thread(target=run,args=(i,))
    t.start()

'''
    当我们在使用锁的过程中使用所两次的话，我们需要对照请求两次也要释放两次
  但是当你换实用Lock的话会出现线程堵塞的情况，这时候需要我们将Lock换用为RLock(RLock带有递归功能)
'''