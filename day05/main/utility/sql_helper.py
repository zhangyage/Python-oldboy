#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb

class MySqlHelper(object):
    def __init__(self):
        pass
    
    def Get_Dict(self,sql,params):
        conn = MySQLdb.connect(host='192.168.75.133',user='zhangyage',passwd='zhangyage',db='oldboy')

        cur = conn.cursor()

        result1=cur.execute(sql,params)
        data = cur.fetchall()     #保存sql执行的结果

        cur.close()
        conn.close()
        return data
    
    def Get_One(self,sql,params):
        conn = MySQLdb.connect(host='192.168.75.133',user='zhangyage',passwd='zhangyage',db='oldboy')

        cur = conn.cursor()

        result1=cur.execute(sql,params)
        data = cur.fetchone()     #保存sql执行的结果

        cur.close()
        conn.close()
        return data
    
helper = MySqlHelper()
sql = 'select * from Userinfo where id > %s'
params = (5,)
print helper.Get_Dict(sql, params)