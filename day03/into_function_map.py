#!/usr/bin/env python
# -*- coding:utf-8 -*-


def Function(arg):
    print arg

Function('argtest')


'''
需求：让一个列表中的元素都+100输出新列表
'''
def foo(arg):
    return arg + 100

li = [11,22,33]

temp = []
for item in li:
    temp.append(foo(item))  #使用append方法调用函数追加列表元素

print temp

#使用map内置函数我们的代码将会少很多，如下：
temp = map(foo,li)       #传入一个函数名和列表名
print temp

#再次进化    代码被缩减到两行了
temp = map(lambda arg:arg+100,li)
print temp


#filter学习，过滤学习
lis = [11,2,222,33]
def bar(arg):
    if arg <22:
        return True
    else:
        return False
temp = filter(bar,lis)   #之过滤返回True的数据
print temp


#reduce学习  做累加和累乘
li = [1,2,3]
print reduce(lambda x,y:x*y,li)     #返回6 累乘  reduce使用的时候，必须传入两个参数


#zip 传入N个列表可以按列生产新的列表
x = [1,2,3,4]
y = [3,4,5,6]
z = [3,6,5,7]
m = [3,7,8,9]
print zip(x,y,z,m)  #[(1, 3, 3, 3), (2, 4, 6, 7), (3, 5, 5, 8), (4, 6, 7, 9)]案列转储为新的列表
#当中间一个列表是3个元素，就会输出三个新的元组，木桶效应