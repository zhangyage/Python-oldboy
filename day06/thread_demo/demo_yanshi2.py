#!/usr/bin/env python
# -*- coding:utf-8 -*-

from threading import Thread
from Queue import Queue
#导入队列模块   队列是先进先出 
import time
import random

def Proudcer(name,que):
    while True:
        if que.qsize() < 5:
            que.put('baozi')
            print '%s:made a baozi....'%name
        else:
            print '还有5个包子'
        time.sleep(random.randrange(2))
    
def Consumer(name,que):
    while True:
        try:
            que.get_nowait()
            print '%s:got a baozi....'%name
        except Exception:
            print u'没有包子。。。'  
        time.sleep(random.randrange(3))  
que = Queue()

p1 = Thread(target=Proudcer,args=('张亚歌1',que))
p2 = Thread(target=Proudcer,args=('张亚歌22',que))
p1.start()
p2.start()

C1 = Thread(target=Consumer,args=('潘远庆1',que))
C1.start()
C2 = Thread(target=Consumer,args=('潘远庆2',que))
C2.start()
C3 = Thread(target=Consumer,args=('潘远庆3',que))
C3.start()
#Proudcer('zhangyage', que)

#Consumer('panyuanqing', que)
    




