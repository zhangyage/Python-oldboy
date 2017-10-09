#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
定义类的方法

函数和方法的区别
函数是直接通过函数名进行调用的
方法是类的一部分需要通过类进行调用
'''

# class Example(object):
#     def add(self):    #公用的方法
#         pass 
#     
#     def _minus(self): #私有方法
#         pass
#     
#     def __multiply(self): 
#         pass

class Programer(object):
    hobby = 'Play computer'
    
    def __init__(self,name,age,weight):
        self.name = name      #类的共有属性
        self._age = age       #私有属性和共有属性差不多
        self.__weight = weight #私有属性  这个属性只有在类内部可以调用    对象是不可以直接调用的
        
    
    @classmethod
    def get_hobby(cls):
        return cls.hobby
    
    @property
    def get_weight(self):
        return self.__weight
    
    def self_introduction(self):
        print 'my name is %s\nI am %s years old\n' %(self.name,self._age)
        

if __name__ == '__main__':
    programer = Programer('zhang',25,75)
    print dir(programer)
    print Programer.get_hobby()    #注意这个和下一个调用方法的方式
    print programer.get_weight
    programer.self_introduction()
    
'''
['_Programer__weight', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_age', 'get_hobby', 'get_weight', 'hobby', 'name', 'self_introduction']
Play computer
75
my name is zhang
I am 25 years old
'''