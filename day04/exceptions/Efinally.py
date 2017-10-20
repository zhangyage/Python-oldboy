#!/usr/bin/env python
# -*- coding:utf-8 -*-

#try》finally  不管是否有异常finally语句都要执行！

try:
    f = open("1.txt")
    print int(f.read())
finally:
    print "file close!"
    f.close()  #关闭文件操作