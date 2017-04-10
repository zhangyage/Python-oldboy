#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
特性（属性）
          需要在动态方法前计入装饰器@property  def Bar(self):
          特性的访问类似于动态字段访问，不在是方法的访问
'''

class Provice:
    
    memo = '省份之一'     #这个值是属于类的         静态字段
    
    def __init__(self,name,capital,leader):   #slef就是你以后创建对象的对象值
        self.Name = name      #这个值属于对象  动态字段
        self.Capital = capital
        self.Leader = leader
        
    def sports_meet(self):           #动态方法
        print self.Name + '开运动会'
        
    @staticmethod                    #静态字段
    def Foo():
        print '每个省都要反复'
        
    @property                        #特性
    def Bar(self):
        #print self.Name
        return 'someting'

hn = Provice('河南','郑州','李克强')
sd = Provice('山东','济南','习近平')
hn.sports_meet()      #对象访问动态方法
sd.sports_meet()
Provice.Foo()         #类访问静态方法

#hn.Bar        #特性访问的时候就不在是以方法的形式进行访问，访问按照字段的形式进行访问
print hn.Bar