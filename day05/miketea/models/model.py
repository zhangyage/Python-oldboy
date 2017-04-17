#!/usr/bin/env python
# -*- coding:utf-8 -*-

from utility.sql_helper import MySqlHelper

class UserInfo:
    
    def __init__(self):
        self.sqlHelper = MySqlHelper()
    
    def CheckLogin(self,name,pwd):
        '''验证用户名的合法性
        @param name:用户名
        @param pwd:密码
        @return: 如果登录成功返回用户ID，否则返回False
        '''
        sql = 'select Nid,Name,Password from UserInfo Name=%s and Password = %s' 
        params = (name,pwd, )
        result = self.sqlHelper.GetSimple(sql, params)
        if not result:
            print False
        else:
            print result['Nid']  
     
class ChatRecord:
    
    def __init__(self):
        self.sqlHelper = MySqlHelper()
    
    def InsertRecord(self,message,date,userid):
        '''插入聊天记录
        @param message:聊天信息
        @param date:时间
        @param userid:用户ID
        @return: 如果聊天插入成功返回True:否则返回False   
        '''
        sql = 'insert into Userinfo(Message,Date,UserID) values(%s,%s,%s)'
        params = (message,date,userid,)
        result = self.sqlHelper.InsSample(sql, params)
        result.commit()
        if not result:
            print False
        else:
            print True  
        
        
    def GetRecord(self,userid):
        '''
        @param userid:用户id 
        '''
        sql = 'select * from ChatRecord where = %s'
        params = (userid,)
        result = self.sqlHelper.GetDict(sql, params)
       
    
    