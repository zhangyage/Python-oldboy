#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
操作数据库驱动
'''

import MySQLdb
import conf

class MySqlHelper(object):
    def __init__(self):
        self.conn_dict = dict(conf.conn_dict)    #导入链接数据库字符串
    
    def GetSimple(self,sql,params):
        '''获取单条数据
        @param sql:sql语句
        @param params:参数
        @return: 数据 
        '''
        conn = MySQLdb.connect(**self.conn_dict)
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        result1=cur.execute(sql,params)
        data = cur.fetchone()     #保存sql执行的结果
        cur.close()
        conn.close()
        return data
                     
    def GetDict(self,sql,params):       #获取多行数据
        '''获取多条数据 '''
        conn = MySQLdb.connect(**self.conn_dict)
        cur = conn.cursor()
        result1=cur.execute(sql,params)
        data = cur.fetchall()     #保存sql执行的结果
        cur.close()
        conn.close()
        return data
    
    def InsSample(self,sql,params):
        '''插入单条数据
        @return: 受影响的条数
        '''
        conn = MySQLdb.connect(**self.conn_dict)
        cur = conn.cursor()
        count=cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
        return count
    
    def InsDict(self,sql,params):
        '''插入多条数据
        @return: 受影响的条数
        '''
        conn = MySQLdb.connect(**self.conn_dict)
        cur = conn.cursor()
        count=cur.executemany(sql,params)
        conn.commit()
        cur.close()
        conn.close()
        return count
    
    def InsSample_ReturnId(self,sql,params):
        '''插入单条数据
        @return: 返回自增id       #自增id作为外键建立关联
        '''
        conn = MySQLdb.connect(**self.conn_dict)
        cur = conn.cursor()
        count=cur.execute(sql,params)
        id = cur.lastrowid
        conn.commit()
        cur.close()
        conn.close()
        return id
        
        
    
