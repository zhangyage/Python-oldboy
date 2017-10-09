#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
定义类的属性
'''


class Programer(object):
    hobby = 'Play computer'
    
    def __init__(self,name,age,weight):
        self.name = name      #类的共有属性
        self._age = age       #私有属性和共有属性差不多
        self.__weight = weight #私有属性  这个属性只有在类内部可以调用    对象是不可以直接调用的
        
    def get_weight(self):
        return self.__weight
    
if __name__ == '__main__':
    programer = Programer('zhang',25,75)
    print dir(programer)
    print programer.__dict__
    print programer.get_weight()
    print programer._Programer__weight
    
'''
['_Programer__weight', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_age', 'get_weight', 'hobby', 'name']
{'_age': 25, '_Programer__weight': 75, 'name': 'zhang'}
75
75
''' 
        