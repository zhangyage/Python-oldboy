#!/usr/bin/env python
# -*- coding:utf-8 -*-


info = '''this is a test 
          what's you name
          my name is zhang'''

print info

#'''号是格式化打印

print ord(':')
#ord可以核实一个字符占用的ASCII的位置


test = "this is a ceshi"
print type(test)

#放在变量赋值的时候，在对应的变量值前放置一个u对应的变量将被赋值问unicode
test1 = u"this is a test"
print type(test1)

#转化对应的变量为Uft-8格式
test1.encode('utf-8')

#decode是将对应的utf-8转换为unicode
test1.decode('utf-8')