#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
字典学习
'''
from day01.zhushi_test import info


info = {'name':'zhangyage','age':'25','phone':'15510367325','address':'henan','sex':'boy'}
print info['name']          #获取字典中key值对应的value

info['salary'] = 3000       #插入元素
print info

info['job'] = 'IT'
print info

print info.popitem()     #字典是没有排序的，因此删除的时候是随机的


for i in info:
    print i              #这个循环得到的是字典中的key的循环，没有value的值
    
    
for i in info:           #遍历输出key，value   效率高
    print i,info[i]
    
for k,v in info.items(): #遍历输出key，value   效率低
    print k,v
    

print info.get('job')           #返回值IT      get()方法是获取一个key对应的value的值，有的话就返回结果，没有的话返回none,和info[]一样的作用，但是后者在没有key值得时候回返回报错
print info.get('jiating')       #返回值None


print info.has_key('job')      #has_key('job')判断字典中是否有对应的key，有的话返回Ture没有的话返回Flase

print info.keys()               #返回字典中所用的key值
print info.values()             #返回字典中所有的value值