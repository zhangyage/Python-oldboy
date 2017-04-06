#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''

'''
#练习四             变态需求，函数仅接受一个参数可以传入多个参数
def show1(arg):
    for item in arg:
        print item ,
    print               #为了区分，print默认是输入换行
        
def show2(arg1,arg2):
    print arg1,arg2

show1(['liyang','alex'])          #输出结果 liyang alex
show2('lingyang','alex')          #输出结果lingyang alex
#上面的测试都是正常的写法，下面值放置一个参数我们传入多个值得方法
def Show(*arg):                #在参数前面添加一个*号，这个传入参数的个数就变化为随机的       常使用在参数不定的情况下，或是参数是列表
    for item in arg:
        print item ,
    print
        
Show('pan','yuan','qing','zhang','yage','guang')
#输出结果pan yuan qing zhang yage guang

def SHOW(**arg):                   #**arg可以传入字典类型的参数
    for k,v in arg.items():
        print k,v 
        
SHOW(zhang='yage',pan='yuanqing',li='guang')
#输出结果li guang pan yuanqing zhang yage
userlist = {'k1':'zhngayge','k2':'panyuanqing'}
SHOW(**userlist)  #当你提前定义字典的话在传入字典时候需要在参数前面添加**