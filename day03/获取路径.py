#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys
import os

print __file__
#获取当前文件的绝对路径

print os.path.dirname(__file__)
#打印当前文件所在的文件夹

#打印上层目录路径    获取绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print BASE_DIR


sys.path.append(BASE_DIR)    #将对应的路径导入python系统环境，这样就可以直接导入下面的模块了
