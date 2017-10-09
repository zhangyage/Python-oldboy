#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utility.sql_helper import MySqlHelper
import datetime

class Gu_info:
    def __init__(self):
        self.sqlHelper = MySqlHelper()  
       
    def Insertdata(self,name,num,pice,Itime=datetime.datetime.now().strftime('%Y-%m-%d')):
        '''插入当天休市股价记录
        @param gu_name:股票名称
        @param gu_num:股票代码
        @param gu_price:股票价格
        @param create_date:插入时间
        @return: 如果聊天插入成功返回True:否则返回False   
        '''
        sql = 'insert into gu_info(gu_name,gu_num,gu_price,create_date) values(%s,%s,%s,%s)'
        params = (name,num,pice,Itime)
        result = self.sqlHelper.InsSample(sql, params)
        
        if not result:
            print False
        else:
            print True  
            
#gupiao = Gu_info()
#gupiao.Insertdata("浦发银行", '603', '19',)\

    
    