#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
继承

新式类    推荐使用
           继承object
    __file__   __doc__  __name__这些都是新式类定义的    类也是object创建的

经典类
            没有继承object
            
在其他语言中都是默认继承object,python继承的object是用c写的
Python实在python2.2后产生的     修复在python中经典类多重继承的bug
'''

#子类  父类   或是（基类 派生类）

class Father(object):
    def __init__(self):
        self.Fname = 'Fname'
        print 'Father.__init__'
    
    def Func(self):
        print 'father.Func'
        
    def Bad(self):
        print 'father.抽烟、喝酒、烫头'
        
class Son(Father):
    def __init__(self):
        self.Sname = 'Sname'
        print 'Son.__init__'
        #Father.__init__(self)  #显示的执行父类的构造函数
        super(Son,self).__init__()  #使用super执行父类的构造函数   这个时候需要我们的父类继承object
        #上面的两种方法执行父类的构造函数
        
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
    