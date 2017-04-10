#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
装饰器学习
装饰器可以在我们为函数批量添加功能时候节省我们的工作量
'''
#装饰器函数
def outer(fun):
    def wrapper(arg):        #传递参数
        print '验证'          #在这里加入一行，在我们再次执行函数的时候就可以在多输出这一喊
        reslute1 = fun(arg)
        return reslute1      #这样使用可以是我们的函数带有返回值
        print '就是这样做的'
    return wrapper

@outer    #和装饰器函数建立关系
def Func1(arg):
    print 'func1',arg
    return '返回在什么位置呢？'
       
respone = Func1('test')
print respone
