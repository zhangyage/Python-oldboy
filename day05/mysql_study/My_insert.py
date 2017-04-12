#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
插入操作
'''

import MySQLdb


conn = MySQLdb.connect(host='192.168.75.133',user='zhangyage',passwd='zhangyage',db='oldboy')

cur = conn.cursor()

sql = "insert into Userinfo(name,address) values(%s,%s)"     #定制sql语句，占位符方便以后参数传入
params = ('guan','shangqiu',)                                 #参数,是必须有的，要不是会报错的
result1=cur.execute(sql,params)                              #sql操作
conn.commit()               #提交数据库       insert update delete事务操作需要commit


cur.close()
conn.close()