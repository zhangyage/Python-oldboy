#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
设置环境变量   方便导入模块
'''

import os,sys
base_dir = os.path.dirname(os.path.dirname(__file__))
#print base_dir
#print __file__   #获取当前文件的执行路径
sys.path.append(base_dir)