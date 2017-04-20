#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time


num = 0

def run(n):
    time.sleep(1)
    global num
    num +=1
    print '%s\n' %num
    
for i in range(100):
    t = threading.Thread(target=run,args=(i,))
    t.start()

'''
    总结：使用如上线程你会发现问题，并没有输出到100会出现数据丢失的问题
'''第二期    Y20170505    V/华记 V1    10    1.3%    M4.5/ 