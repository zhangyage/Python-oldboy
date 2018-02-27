#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

#查看操作系统
print os.name

#获取工作目录
print os.getcwd()

#获取某个目录下的所有文件名
print os.listdir('E:\workspace\Python-oldboy')

#运行一个shell命令   调用计算器
# os.system("calc")

#删除某个文件
#os.remove("E:\workspace\Python-oldboy\my_study\sys_study")

#判断是文件还是文件夹
print os.path.isfile("E:\workspace\Python-oldboy\my_study\sys_study\oneos.py")
print os.path.isdir("E:\workspace\Python-oldboy\my_study\sys_study")

#路径拆分  把完整路径分为目录+文件名

print os.path.split("E:\workspace\Python-oldboy\my_study\sys_study\oneos.py")
#结果  ('E:\\workspace\\Python-oldboy\\my_study\\sys_study', 'oneos.py')

print os.path.split("E:\workspace\Python-oldboy\my_study\sys_study")
#结果  ('E:\\workspace\\Python-oldboy\\my_study', 'sys_study')
print os.path.split('E:\workspace\Python-oldboy\my_study\')
#结果  ('E:\\workspace\\Python-oldboy\\my_study')
#注意后两个就是最后面是否有\有的话是目录，没有的话是文件