#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
继承
'''

#子类  父类   或是（基类 派生类）

class Father:
    def __init__(self):
        self.Fname = 'Fname'
    
    def Func(self):
        print 'father.Func'
        
    def Bad(self):
        print 'father.抽烟、喝酒、烫头'
        
class Son(Father):
    def __init__(self):
        self.Sname = 'Sname'
        
    def Bar(self):
        print 'son.Func'
    
    '''    
    def Bad(self):       #重写父类的方法
        print 'son.不抽烟喝酒'
    '''    
    def Bad(self):        #继承父类的方法同时自己有多了一些问题，叠加
        Father.Bad(self)
        print 'son.赌博'
               
s1 = Son()       #实例化s1
s1.Bar()         #调用自己的动态方法
s1.Func()        #调用父类的动态方法
s1.Bad()         #重写父类的方法（或是问题叠加）   
    