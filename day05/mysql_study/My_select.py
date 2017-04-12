#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
mysql查询操作
1、创建链接
2、创建游标
3、执行数据
      数据处理
4、关闭游标
5、关闭链接
'''
import MySQLdb


conn = MySQLdb.connect(host='192.168.75.133',user='zhangyage',passwd='zhangyage',db='oldboy')

cur = conn.cursor()

result1=cur.execute('select * from Userinfo')
data = cur.fetchall()     #保存sql执行的结果

cur.close()
conn.close()

print result1          #这个输出的是查询时候影响的行数
print data             #输出查询结果 是元组的形式
