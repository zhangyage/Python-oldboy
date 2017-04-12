#!/usr/bin/env python
# -*- coding:utf-8 -*-

#syntax语法   indent缩进
#例子一：变量没有定义
try:
    print i
except NameError:
    i=9
    i+=10
    print "刚才的i没有定义，处理异常后，i的值为："+str(i)


#例子二：处理多种异常
try:
    #i="zhang"
    #j=0
    print i+j 
except NameError:
    i=j=0
    print "刚才的i或j没有进行初始化数据，现在我们将其初始化为0，结果是："
    print i+j
except TypeError:
    print "刚刚i与j的类型对应不上，我们转换一下类型即可处理异常，处理后：结果是："+str(i)+str(j)
   