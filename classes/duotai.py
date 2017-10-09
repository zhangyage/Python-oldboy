#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
类的多态
   主要涉及的是类的继承和重写
'''

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
    
class BackendProgramer(Programer):
    def __init__(self,name,age,weight,language):
        '''
        @super 使用super调用父类的方法   属性
        '''
        super(BackendProgramer,self).__init__(name, age, weight)
        self.language = language  
        
    def self_introduction(self):
        print 'My name is %s\nMy favorite language is %s' %(self.name,self.language)


#判断继承关系
def introduce(programer):
    if isinstance(programer, Programer):
        programer.self_introduction()
        
        
if __name__ == '__main__':
    programer = Programer('pan',24,70)
    backend_programer = BackendProgramer('zhang',25,75,'python')
    
    introduce(programer)
    introduce(backend_programer)