#!/usr/bin/env python
# -*- coding:utf-8 -*-



'''
类的学习
'''

class Person:
    def __init__(self,name):#定义方法  这里的self是必须的，所有的方法，第一个参数必须是self,代表所有的实例可以共享他，不具备其他任何意义
        self.name = name

p1 = Person('zhang')  #实例化对象
print p1.name

#使用方法，方法的调用必须通过方法调用，类是不可以直接调用方法的，不能使用抽象的类调用方法必须使用具体的实例调用方法

print p1.__dict__              #输出{'name': 'zhang'}
print dir(p1)                  #输出所有的变量和字段['__doc__', '__init__', '__module__', 'name']