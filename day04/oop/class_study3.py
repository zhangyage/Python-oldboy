#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
静态方法   动态方法
动态方法：sports_meet(self) 
                   对象是可以访问动态方法的，类是不可以访问的
静态方法： 需要先添加装饰器 @staticmethod   Foo()一定不要有self,因为静态方法属于类
                   静态方法属于类，类是可以访问类的
'''
class Provice:
    
    memo = '省份之一'     #这个值是属于类的         静态字段
    
    def __init__(self,name,capital,leader):   #slef就是你以后创建对象的对象值
        self.Name = name      #这个值属于对象  动态字段
        self.Capital = capital
        self.Leader = leader
        
    def sports_meet(self):           #动态方法
        print self.Name + '开运动会'
        
    @staticmethod                     #静态方法
    def Foo():
        print '每个省都要反复'

hn = Provice('河南','郑州','李克强')
sd = Provice('山东','济南','习近平')
hn.sports_meet()      #对象访问动态方法
sd.sports_meet()
Provice.Foo()         #类访问静态方法
