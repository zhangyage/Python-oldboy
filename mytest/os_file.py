#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

print os.path.abspath(os.path.dirname(__file__))
#print os.path.dirname(__file__)

basedir =  os.path.abspath(os.path.dirname(__file__))  #获取当前文件所在的文件夹
print os.path.join(basedir, 'data.sqlite')    #平和路径创建文件