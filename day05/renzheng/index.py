#!/usr/bin/env python
# -*- coding:utf-8 -*-

from model.admin import Admin

def main():
    user = raw_input('输入用户名：')
    pwd = raw_input('输入密码：')
    
    admin = Admin()
    result1 = admin.CheckValidate(user, pwd)
    #print result1    
    if not result1:
        print '用户名密码错误！'
    else:
        print '进入后台管理页面'
    

if __name__ == "__main__":
    main()