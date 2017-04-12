#!/usr/bin/env python
# -*- coding:utf-8 -*-

#try。。。finally:
#如果发生异常的时候现在执行finally下面的语句在执行try报错

'''
#实例一
try:
    #i=7
    print i
finally:
    print "不管上面的是否有异常，我必须进行输出"
'''

#实例二
#要实现将一字符串输出100000000次，假如异常发生，需要知道我们已经输出了多少次
try:
    for i in range(10000000):
        print "我要输出100000000次，但是我现在不知道已经输出了多少次！"
finally:
    print "此时i的值为："+str(i)+"--并没有完全输出"