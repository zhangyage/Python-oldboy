#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
模块联系，有些命令在windows下是没有的
'''

import os

os.system('df')
#df命令在windows命令是没有的，只能在linux系统中使用
os.system('dir')
#windows下dir命令列出文件

print os.walk('.') 



import commands
res = commands.getstatusoutput('pwd')
# commands.getstatusoutput()返回的是一个元组，包括执行的状态和结果
#类似(0,'/root/py/test.py')

import sys

sys.argv  #这个可以打印出在执行相关的py脚本是后面跟的参数，对应的输出结果是个列表


from sys import argv
#如上到如可以直接使用argv方法，节省代码
from multiprocessing as multi
#代码别名定义