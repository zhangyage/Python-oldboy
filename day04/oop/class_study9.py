#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
新式类 与经典类bug调试

新式类    推荐使用
           继承object
    __file__   __doc__  __name__这些都是新式类定义的    类也是object创建的

经典类
            没有继承object
            
在其他语言中都是默认继承object,python继承的object是用c写的
Python实在python2.2后产生的     修复在python中经典类多重继承的bug
'''

#B C继承A
#D继承B C

class A(object):                           #先使用经典类练习
    def __init__(self):
        print 'This is A'
    def save(self):
        print 'save method from ---A---'
        
class B(A):
    def __init__(self):
        print 'This is B'

        
class C(A):
    def __init__(self):
        print 'This is C'
    def save(self):
        print 'save method from ---C---'
        
class D(B,C):                   #多继承继承B,C
    def __init__(self):
        print 'This is D'
        
test = D()
test.save()     #当D继承  class D(B,C):时候是，这个B,C顺序很重要的，顺序执行，得到的确实A的save方法，使用新式类时候就可以继承C的save方法，推荐广度优先

'''
当A是经典类输出            深度优先
This is D
save method from ---A---

当A是新式类输出            广度优先---建议使用
This is D
save method from ---C---

'''