#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
类的属性的访问控制的 魔术方法
1、设置对应属性   __setattr__(self,name,value)
2、设置对应属性   __delattr__(self,name,value)
'''

class Programer(object):
    def __init__(self,name,age):
            self.name = name      
            self.age = age       
    
    def __getattribute__(self,name):
        #return getattr(self, name)  #使用这个方法会导致无限递归
        return super(Programer,self).__getattribute__(name)
    
    def __setattr__(self, name,value):
        #setattr(self,name,value)     #使用这个方法会导致无限递归
        self.__dict__[name] = value    

      
if __name__ == '__main__':
    p1 = Programer('zhang',25)
    print p1.name
    

'''
zhang is 25 years old
['age', 'name']
'''