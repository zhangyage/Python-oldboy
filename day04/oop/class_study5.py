#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
私有方法和私有字段
私有字段：self.__Thailand
               私有字段是不能直接被对象和类进行访问的，需要通过动态方法访问
               同样私有字段也是可以通过特性的方法访问的
私有方法：
              私有方法是不能直接被对象和类进行访问的，通过使用动态方法进行访问
      japan._Provice__sha()   #显示调用私有方法，但是不建议这么使用
      
私有字段使用字段，可以让被人访问，但是不可以让别人改动
'''

class Provice:
    
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
        
    @property                      #通过特性访问私有字段
    def Thailand(self):
        return self.__Thailand
#hn = Provice('河南','郑州','李克强')
#sd = Provice('山东','济南','习近平')


japan = Provice('日本','东京','安倍',True)
#print japan.__Thailand          #访问报错   AttributeError: Provice instance has no attribute '__Thailand'
#对象是不能直接访问私有字段的

japan.show()            #私有字段需要使用动态方法进行访问输出


japan.Foo2()            #私有方法通过使用动态方法进行访问输出
japan._Provice__sha()   #显示调用私有方法，但是不建议这么使用

print japan.Thailand    #通过特性访问私有字段 