#!/usr/bin/env python
# -*- coding:utf-8 -*-

from threading import Thread
from Queue import Queue
#导入队列模块   队列是先进先出 
import time



class Procuder(Thread):
    def __init__(self,name,queue):
        '''
        @param name:生产者的名称
        @param queue:容器
        '''
        self.__Name = name
        self.__Queue = queue
        super(Procuder,self).__init__()   #继承一下父类的使用方法   执行父类的构造函数
    
    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(1)
            else:
                self.__Queue.put('包子')
                time.sleep(1)
                print '%s 生产了一个包子' % (self.__Name,)
        
        
class Consumer(Thread):
    def __init__(self,name,queue):
        '''
        @param name:生产者的名称
        @param queue:容器
        '''
        self.__Name = name
        self.__Queue = queue
        super(Consumer,self).__init__()   #继承一下父类的使用方法   执行父类的构造函数
    
    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(1)
            else:
                self.__Queue.get('包子')
                time.sleep(1)
                print '%s 消费了一个包子' % (self.__Name,)
        
que = Queue(maxsize=100)

zhang1 = Procuder('张亚歌1',que)
zhang1.start()

zhang2 = Procuder('张亚歌22',que)
zhang2.start()


zhang3 = Procuder('张亚歌333',que)
zhang3.start() 

for item in range(20):
    name = 'pan%d' %(item,)
    temp = Consumer(name,que)
    temp.start()























