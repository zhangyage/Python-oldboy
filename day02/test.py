#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
查出一个列表中zhangyage元素的位置，请输出结果
'''

name_list = ['zhangyage', 'panyuanqing', 'zhangyage', 'liuchangcai', 'guanshuolei', 'zhangyage', 'zhangyage']
'''
方法一
'''
first_pos = 0
for i in range(name_list.count('zhangyage')):
    new_list = name_list[first_pos:]
    next_pos = new_list.index('zhangyage') +1
    print 'Find postion',first_pos+next_pos
    first_pos += next_pos

'''
方法二
'''  
names_list = ['zhangyage', 'panyuanqing', 'zhangyage', 'liuchangcai', 'guanshuolei', 'zhangyage', 'zhangyage']
pos=1
for i in range(names_list.count('zhangyage')):
    if i == 0:
        pos = names_list.index('zhangyage') 
    else:
        pos = names_list.index('zhangyage',pos+1)
    print pos+1 
    