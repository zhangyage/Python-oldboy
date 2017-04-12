#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
mysql查询操作
fetchall()和fetchone()比较
fetchall()   #获取所有的数据
fetchone()   #只获取一条数据

cur.scroll(0,mode='absolute')   #绝对定位，可以定位指针的位置结合yeild学习  0代表的是开头
cur.scroll(-1,mode='relative')   #相对定位，-1是将指针退回一个，
'''
import MySQLdb


conn = MySQLdb.connect(host='192.168.75.133',user='zhangyage',passwd='zhangyage',db='oldboy')

cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

result1=cur.execute('select * from Userinfo')
data = cur.fetchone()     #保存sql执行的结果
print data                #输出第一条

#cur.scroll(0,mode='absolute')   #绝对定位，将指针知道开始，这样两次的输出结果是相同的
cur.scroll(-1,mode='relative')   #相对定位，将指针退回一个，这样两次的输出结果是相同的

data = cur.fetchone()     #保存sql执行的结果
print data                #输出第二条

cur.close()
conn.close()

#print result1          #这个输出的是查询时候影响的行数
#print data             #输出查询结果 是元组的形式
