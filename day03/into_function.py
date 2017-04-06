#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
常见的内置函数
dir()
help()
'''

a = []
print help(a)        #获取帮助信息
print dir()          #获取对象可以使用的方法，输出的是key值
print vars()         #和dir()一样，但是vars输出的是key:values的字典形式
print type(a)        #查看对应参数的类型

print abs(-40)       #abs球绝对值
print bool(-1)       #bool布尔判断，只有后面的值是0的时候返回flase

print divmod(9,4)    #返回(2, 1)  返回的结果是商和余数
print divmod(9,2)    #返回(4, 1)

print max([11,22,33,333])   #求最大值
print min([11,22,33,333])   #求最小值
print sum([11,22,33,333])   #求和
print pow(2,10)             #返回1024  指数运算

print len('zhonghuarenmin') #字符串的长度，也可以是列表和字典

print all([1,2,3,4,0])      #返回False  判断迭代元素中有一个为0就返回False
print all([1,2,3,4,1])      #返回True

print any([0,0,0,0,0,0,0])  #返回False 判断后面的迭代元素都为0的话返回False
print any([0,0,0,0,0,0,1])  #返回True  有一个为真就返回True

print chr(97)               #返回a chr是将某个AscII码转换为字符
print ord('a')              #返回97  ord是将某个字符转换为AscII码

print hex(20)               #16进制
print bin(2)                #2进制
print oct(2)                #8进制

jiating = ['房子','车子','孩子','票子']
for item in jiating:
    print item
    
for item in enumerate(jiating,1):  #enumerate(jiating,1)输出会带有索引号，,1是指定索引开始的位置
    #print item
    print item[0],item[1]


print ('{0},study {1}'.format('zhangyage','python'))     #format格式化输出