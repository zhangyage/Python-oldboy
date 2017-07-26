#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

#将uninx转换为date的时间格式
def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format,value)
    return dt

def datetime_timestamp(value):
    time.strptime(value, '%m/%d/%Y:%H:%M:%S')
    #将字符串转化为指定的时间元组格式
    s = time.mktime(time.strptime(value, '%m/%d/%Y:%H:%M:%S'))
    return s

print timestamp_datetime(1332888820)

unix = '10/7/2017:22:52:02'
print  datetime_timestamp(unix)