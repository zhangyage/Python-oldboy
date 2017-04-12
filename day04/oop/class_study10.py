#!/usr/bin/env python
# -*- coding:utf-8 -*-
from _pyio import __metaclass__


'''
接口定义和规范设计

抽象类加抽象方法就叫接口
'''

from abc import ABCMeta, abstractmethod   #下面的定义接口是的固定设计
class Alert:
    __metaclass__ = ABCMeta
    
    @abstractmethod                 #指定接口的方法，在继承接口是必须定义这个方法，要不报错
    def Send(self):
        pass
    
class Weixin(Alert):       #继承接口类
    def __init__(self):
        print '__init__'
        
    def Send(self):        #必须定义接口中定义的方法名称，保证程序不报错和开发的规范
        print 'send.weixin'
        
f=Weixin()
f.Send()