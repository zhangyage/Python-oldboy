#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

'''
析构函数   __del__
               析构函数函数在所有对象都不引用的时候销毁，释放内存
               这个函数都只最后一次执行
               
构造方法  __init__
                构造方法是在实例化对象是一定执行的方法
call方法 __call__
                实例化对象后使用'对象()'直接可以执行call方法  比较变态  其他编程语言中没有这个用法
'''


class Foo:
    def __init__(self):   #构造函数
        pass
    
    def __del__(self):    #析构函数     在类执行完以后就会执行这个
        print '解释器销毁我了，我要做最后一次呐喊'
        
    def __call__(self):
        print 'call方法'
    
f1 = Foo()  #想当于执行__init__方法

time.sleep(10)   #等待10秒后才会往下执行，只有执行完成后才会执行析构函数

f1()        #这个就是执行类里面的call方法