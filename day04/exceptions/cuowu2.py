#!/usr/bin/env python
# -*- coding:utf-8 -*-

#异常的引发
#实例一
'''
#使用raise手动引发一个错误： 使用rasie引发一个系统异常
i= 8
if i > 7:
    print 9
    raise NameError
    print 10
''' 
'''
#实例二
#自定义一个类（异常）         #系统的异常时自动引发的，自定义的异常必须使用raise异常
class RhhError(Exception):   #安装命名规范，以Error结尾，并定义异常需要继承的Exception类
    def __init__(self):
        Exception.__init__(self)
        
try:
    i = 8
    if i>7:
        raise RhhError     #引发异常
except RhhError,yhg:       #yhg是Rhh的一个异常实例化
    print "错了就是错了"
'''    
    
#实例三
#自定义一个多参数的异常并用raise引发，比如我们定义一个异常，当x>2或者x+y>7的时候都会引发异常
class HhhError(Exception):
    def __init__(self,x,y):
        Exception.__init__(self,x,y)   #初始化操作
        self.x=x
        self.y=y 
try:
    x=10
    y=0
    if x>2 or x+y>7:
        raise HhhError(x,y)
except HhhError:
    print "HhhError,相关要求x<2或者x+y<=7"  