#!/usr/bin/env python
# -*- coding:utf-8 -*-
#启动页面

import os

list1 = []

b =  os.walk('D:\workspace\Python-oldboy')
#返回的是一个三元元组为元素的列表，每个列表代表的是一个文件夹的内容
for i in b:
    for j in i[2]:
        list1.append(os.path.join(i[0],j))
print len(list1)
