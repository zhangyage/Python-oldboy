#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
更新操作
'''

import MySQLdb


conn = MySQLdb.connect(host='192.168.75.133',user='zhangyage',passwd='zhangyage',db='oldboy')

cur = conn.cursor()

sql = "update Userinfo set name = %s where id = %s"     #定制sql语句，占位符方便以后参数传入
params = ('shao','6')                                    #参数
result1=cur.execute(sql,params)                              #sql操作
conn.commit()               #提交数据库       insert update delete事务操作需要commit


cur.close()
conn.close()