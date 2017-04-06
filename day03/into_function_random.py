#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
random生成随机数
'''
import random

print random.random()          #生成0-1之间的随机数
print random.randint(1,2)      #生成区间的随机数，包括1,2
print random.randrange(1,10)   #生成区间的随机数，不包括10


#写一个随机验证码的程序
code = []
for i in range(6):
    if i == random.randint(1,5):
        code.append(str(random.randint(1,5)))         #追加列表元素并格式化一下数字为字符
    else:
        temp = random.randint(65,97)
        code.append(chr(temp))
print ''.join(code)                                   #拼合列表为字符串
