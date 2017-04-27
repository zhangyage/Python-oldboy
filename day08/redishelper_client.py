#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
命令行下执行

先执行这个客户端，打开订阅通道然后在执行服务端，服务端开启后会发送订阅信息客户端接受
'''

from  redishelper import RedisHelper

r = RedisHelper()
recv = r.subscribe()
print recv.parse_response()