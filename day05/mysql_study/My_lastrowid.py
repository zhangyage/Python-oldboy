#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
lastrowid 获取自增id
主要使用在外键  表与表之间建立关联 
'''

import MySQLdb


conn = MySQLdb.connect(host='192.168.75.133',user='zhangyage',passwd='zhangyage',db='oldboy')

cur = conn.cursor()

sql = "insert into media(address) values(%s)"     #定制sql语句，占位符方便以后参数传入
params = ('usr/local/bin',)                                  #参数  ,是必须有的，要不是会报错的
result1=cur.execute(sql,params)                              #sql操作
conn.commit()               #提交数据库       insert update delete事务操作需要commit
new_id = cur.lastrowid      #获取刚添加元素的id值，用来作为数据插入到其他表，是两个表之间建立关联
print new_id

cur.close()
conn.close()