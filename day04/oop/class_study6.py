#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
只读特性和可写特性           主要针对的是私有字段的修改的操作
只读特性  @property
               这个特性可以通过对象访问私有动态字段的方法访问到私有字段

可写特性 @Thailand.setter  def Thailand(self,value):
               这个方法使我们可以灵活的修改我们的私有字段，提高了程序的灵活性

'''

class Provice(object):          #配合可改特性，继承object
    
    memo = '省份之一'     #这个值是属于类的         静态字段
    
    def __init__(self,name,capital,leader,flag):   #slef就是你以后创建对象的对象值
        self.Name = name         #这个值属于对象  动态字段
        self.Capital = capital
        self.Leader = leader
        
        self.__Thailand = flag    #私有字段
        
    def show(self):                  #访问私有字段
        print self.__Thailand
        
    def __sha(self):                #定义私有方法
        print '我是Alex'
        
    def Foo2(self):                #通过动态方法访问私有方法
        self.__sha()
    
    #只读   私有字段
    @property                      #通过特性访问私有字段
    def Thailand(self):
        return self.__Thailand
    
    #可改   私有字段   装饰器就是方法名.setter   同时还需要类继承object   推荐使用私有字段的方法
    @Thailand.setter 
    def Thailand(self,value):
        self.__Thailand = value

japan = Provice('日本','东京','安倍',True)
#print japan.__Thailand          #访问报错   AttributeError: Provice instance has no attribute '__Thailand'
#对象是不能直接访问私有字段的
'''
japan.show()            #私有字段需要使用动态方法进行访问输出


japan.Foo2()            #私有方法通过使用动态方法进行访问输出
japan._Provice__sha()   #显示调用私有方法，但是不建议这么使用

print japan.Thailand    #通过特性访问私有字段 
'''
print japan.Thailand
japan.Thailand = False    #修改可改特性
print japan.Thailand
#如果注释掉Thailand.setter就不可以修改了