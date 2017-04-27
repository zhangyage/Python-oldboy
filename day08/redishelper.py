#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis


class RedisHelper:
    
    def __init__(self):
        self.__conn = redis.Redis(host='192.168.75.133')
        self.chan_sub = 'fm87.7'
        self.chan_pub = 'fm87.7'
    
    #获取数据    
    def get(self,key):
        return self.__conn.get(key)
    
    #插入数据
    def set(self,key,value):
        self.__conn.set(key,value)
        
    #发布数据
    def public(self,msg):
        self.__conn.publish(self.chan_pub, msg)  #发布到对应的频道相关的信息
        return True
    
    #订阅数据
    def subscribe(self):
        pub = self.__conn.pubsub()     #打开频道
        pub.subscribe(self.chan_sub)   #订阅频道
        pub.parse_response()           #等待接受
        return pub
    
if __name__ == '__main__':
    t = RedisHelper()
    t.public('test')