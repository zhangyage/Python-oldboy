#!/usr/bin/env python
# -*- coding:utf-8 -*-

from threading import Thread
from Queue import Queue
#导入队列模块   队列是先进先出 

class Procuder(Thread):
    def run(self):
        Thread.run(self)
        
        
class Consumer(Thread):
    def run(self):
        Thread.run(self)
        
que = Queue(maxsize=100)
print que.qsize()   #打印队列中元素的个数
que.put(1)          #向队列中添加元素
que.put(2)
que.put(3)
print que.qsize()   
que.put(4)
que.put(5)
que.put(6)
print que.qsize()
print que.empty()        #判断队列是否为空，为空返回True
print 'get:' ,que.get()  #获取队列的元素，一次取得一个先进先出

