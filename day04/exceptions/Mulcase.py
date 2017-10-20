#!/usr/bin/env python
# -*- coding:utf-8 -*-

#多异常捕获
try:
    f = open("1.txt")
    line = f.read(2)
    num = int(line)
    print "read num=%d" % num
except IOError,e:   #捕获没有文件的错误
    print "cathe IOError:",e
except ValueError,e: #捕获文件中的文件必须是数字
    print "cathe ValueError:",e
else:        #程序正常执行的时候才执行这一句
    print "NO Error!"
    