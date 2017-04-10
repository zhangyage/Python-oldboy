#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
time学习
'''

import time

print time.time()          #当前时间戳输出
print time.localtime()     #time.struct_time(tm_year=2017, tm_mon=4, tm_mday=7, tm_hour=14, tm_min=2, tm_sec=56, tm_wday=4, tm_yday=97, tm_isdst=0)
                           #已元组展示的时间
print time.gmtime()        #time.struct_time(tm_year=2017, tm_mon=4, tm_mday=7, tm_hour=6, tm_min=2, tm_sec=56, tm_wday=4, tm_yday=97, tm_isdst=0)

print time.strftime('%Y-%m-%d %H:%M:%S')  #自己格式化当前的时间格式存储
#输出2017-04-07 14:07:33

#上面展示了三种之间，分别是时间戳，结构化的时间和自定义格式(字符串格式)的时间这三种时间也是可以相互转换的
print time.strptime('2017-04-07','%Y-%m-%d')    #将字符串时间格式的时间格式化为结构化的时间格式
print time.mktime(time.localtime())             #将结构化的数据转换为时间戳