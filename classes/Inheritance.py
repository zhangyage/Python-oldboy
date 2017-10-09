#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
继承
提高代码复用
如果没有继承任何父类，建议继承object类

子类：会继承父类的属性和方法
            可以自定义，或是覆盖父类的属性和方法
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

if __name__ == '__main__':
    programer = BackendProgramer('zhang',25,75,'python')
    print dir(programer)
    print programer.__dict__
    print type(programer)
    print isinstance(programer, Programer)
    #isinstance  判断对应是否属于一个类的子类


