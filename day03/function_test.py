#!/usr/bin/env python
# -*- coding:utf-8 -*-

#练习一
def login(username):
    if username == 'zhang':
        print "登录成功！"
    else: 
        print "登录失败！"
        
if __name__ == "__main__":
    user = raw_input("Please input your name:")
    login(user)
    
#练习二        传递二两参数
def Foo(name,action):
    print name,'去',action
    
Foo('zhangyage','北京')
Foo('panyuanqing','信阳')
#输出结果              zhangyage 去 北京                   panyuanqing 去 信阳


#练习三     传递两个参数，其中的一个参数默认赋值
def Bar(name,city='北京'):             
    #print name,'from',city
    print ("{0}'s from {1}".format(name,city))
    
Bar('zhangyage', '上海')               #当使用函数时候再次传入两个参数两个参数会同时传入
Bar('panyuanqing')                    #当仅传入一个参数的时候，第二个参数按照默认值传入
#输出结果           zhangyage's from 上海                panyuanqing's from 北京
    