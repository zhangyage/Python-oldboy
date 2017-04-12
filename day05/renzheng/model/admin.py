#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utility.sql_helper import MySqlHelper

class Admin(object):
    
    def __init__(self):
        self.__helper = MySqlHelper()       #实例化
        
        
    def Get_one(self,id):                   #得到一行数据
        sql = "select * from admin where id = %s"
        params = (id,)
        return self.__helper.Get_One(sql, params)
    
    
    def CheckValidate(self,username,password):  #验证数据的有效性
        sql = "select * from admin where name=%s and password = %s"
        params = (username,password,)
        return self.__helper.Get_One(sql, params)
                
