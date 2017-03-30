#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
集合学习
不会有重复元素
集合是无序的
是可变的，可以添加数据
'''

name = {'zhang','pan','liu','guan'}
print name
name.add('zhang')   #添加元素，当列表中是有对应的元素中，添加时无效的
print name
name.add('li')      #添加集合中不存在的元素是可以正常添加的
print name

#两个集合x\y
x = {1,2,3,4}
y = {3,4,5,6}
print x & y          #交集
print x | y          #并集
print x - y          #差集    输出的是x中有的y中没有的
print x ^ y          #交集的补集         或是堆成差集

z = {1,2,3}
print z.issubset(x)   #判断z是否是x的子集
print x.issuperset(z) #判断x是否包含zqs