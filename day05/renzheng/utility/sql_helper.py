#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb
import conf

class MySqlHelper(object):
    def __init__(self):
        self.conn_dict = dict(conf.conn_dict)    #导入链接数据库字符串
                         #{host:'192.168.75.133',user:'zhangyage',passwd:'zhangyage',db:'oldboy'}
    def Get_Dict(self,sql,params):       #获取多行数据
        conn = MySQLdb.connect(**self.conn_dict)

        cur = conn.cursor()

        result1=cur.execute(sql,params)
        data = cur.fetchall()     #保存sql执行的结果

        cur.close()
        conn.close()
        return data
    
    def Get_One(self,sql,params):             #获取一行数据
        conn = MySQLdb.connect(**self.conn_dict)

        cur = conn.cursor()

        result1=cur.execute(sql,params)
        data = cur.fetchone()     #保存sql执行的结果

        cur.close()
        conn.close()
        return data
    
#helper = MySqlHelper()
#sql = 'select * from Userinfo where id > %s'
#params = (5,)
#print helper.Get_Dict(sql, params)