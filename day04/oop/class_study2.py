#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
类的学习-静态字段
1、静态字段属于类
2、动态字段属于对象
3.属于对象的字段使用  对象.字段 调用   属于类的字段使用  类.字段 调用
4.对象可以访问静态字段，但是动态字段类是不可以访问的
'''

class Provice:
    
    memo = '省份之一'     #这个值是属于类的         静态字段
    
    def __init__(self,name,capital,leader):   #slef就是你以后创建对象的对象值
        self.Name = name      #这个值属于对象  动态字段
        self.Capital = capital
        self.Leader = leader

hn = Provice('河南','郑州','李克强')
sd = Provice('山东','济南','习近平')
print sd.Capital        #属于对象的字段使用  对象.调用
print Provice.memo      #属于类的字段使用  类.调用
print sd.memo           #对象访问静态字段


