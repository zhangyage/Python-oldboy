#!/usr/bin/env python
# -*- coding:utf-8 -*-

L=[('b',6),('a',1),('c',3),('d',4)]
L.sort(lambda x,y:cmp(x[1],y[1]))
#cmp 函数是求出最大的一个
print L