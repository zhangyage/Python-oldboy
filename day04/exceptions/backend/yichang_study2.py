#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
自定义异常：继承Exception
__str__有个特性就是实例化对象之后，print 对象  就可以输出__str__的返回值
'''


class MyException(Exception):
    
    def __init__(self,msg):
        self.error = msg
    
    def __str__(self, *args, **kwargs):   #__str__有个特性就是实例化对象之后，print 对象  就可以输出__str__的返回值
        return self.error
    
#obj = MyException('test')
#print obj           #输出test


raise MyException('自定义错误')   #raise  主动触发异常