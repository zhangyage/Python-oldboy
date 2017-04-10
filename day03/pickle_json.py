#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
序列化和json
序列化是采用特殊的二进制方式处理一下，序列化也支持反序列化
pickle可以序列化一切数据类型
json只能提供常规的数据格式的序列化
'''
import pickle
li = ['zhang','pan','liu','guan','li']
b =  pickle.dumps(li)        #dumps序列化字符串
 
print pickle.loads(b)        #loads反序列化输出


pickle.dump(li,open('temp.pk','w'))         #dump序列化到文件中
print pickle.load(open('temp.pk','r'))      #load反序列化读取文件

import json
name_dic = {'name':'zhang','age':25}
temp = json.dumps(name_dic)
print json.loads(temp)