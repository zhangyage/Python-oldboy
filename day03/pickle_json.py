#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
序列化和json
序列化是采用特殊的二进制方式处理一下，序列化也支持反序列化
'''
import pickle
li = ['zhang','pan','liu','guan','li']
b =  pickle.dumps(li)        #序列化字符串
 
print pickle.loads(b)        #反序列化输出