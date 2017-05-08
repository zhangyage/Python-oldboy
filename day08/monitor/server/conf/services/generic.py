#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
通用的
定义的是基本的监控项目  service
'''

class BaseService(object):
    def __init__(self):
        self.name = 'BaseService'
        self.interval = 300    #监控间隔
        self.last_time = 0
        self.plugin_name = 'your_plugin' #监控插件
        self.triggers = {}     #监控阈值