#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
链接redis
'''

import redis


conn = redis.Redis(host='192.168.75.133')   #创建链接
conn.set('pan','yuanqing')    #在redis中添加一个元素
print conn.get('pan')         #通过key得到元素