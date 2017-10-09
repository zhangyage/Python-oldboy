#!/usr/bin/env python
# -*- coding:utf-8 -*-


import yaml
obj = yaml.load(
'''
 - zhangayge
 - liuzhangcai
 - guanshuolei
 - panyuanqing
'''   
  )

print obj

#结果输出如下：['zhangayge', 'liuzhangcai', 'guanshuolei', 'panyuanqing']