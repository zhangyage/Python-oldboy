#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
插入操作
'''

import MySQLdb


conn = MySQLdb.connect(host='47.94.188.237',user='zhangyage',passwd='Zhang123',db='gudb')

cur = conn.cursor()

sql = "insert into gu_info(gu_name,gu_num,gu_price,create_date) values(%s,%s,%s,%s)"     #定制sql语句，占位符方便以后参数传入
params = ('振华股份', '603', '19','2017-09-15 00:00:50',)                                 #参数,是必须有的，要不是会报错的
result1=cur.execute(sql,params)                              #sql操作
conn.commit()               #提交数据库       insert update delete事务操作需要commit


cur.close()
conn.close()