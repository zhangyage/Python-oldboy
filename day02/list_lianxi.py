#!/usr/bin/env python
# -*- coding:utf-8 -*-

name_list = ['panyuanqing','zhangyage','liuchangcai','guanshuolei']
print name_list[1]                  #输出列表对应的元素，默认从0计数

name_list.append('zhangyage')       #在列表中添加元素，默认添加在最好
print name_list

name_list.insert(0,'zhangyage')     #在第一个元素前插入zhangyage
print name_list

name_list.remove('guanshuolei')     #移除元素guanshuolei
print name_list

print name_list.count('zhangyage')  #统计zhangyage在列表中的次数

print name_list.index('liuchangcai')#列出列表中对应元素的位置，列表是有序的

name_list.pop()                     #默认删除最后 一个元素
print name_list

#name_list.reverse()     #翻转
#name_list.sort()        #排序
#name_list.extend(a)      #扩展  a也是列表，想当于列表相加
print name_list[2:5]      #列表切割，有头没有尾
print name_list[::-1]     #逆序输出
print name_list[1::2]     #从1开始步长为2输出
