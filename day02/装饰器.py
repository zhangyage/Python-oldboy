#!/usr/bin/env python
# -*- coding:utf-8 -*-


user_status = False #用户登陆的时候修改为True

def login(auth_type):   #高阶函数和闭包
    def outer(func):
        def inner(*args,**kwargs):   
        #传递参数，*args传递不定长的参数，**kwargs传递字典类型的参数
            _username = "alex" #
            _password = "abc123"
            global user_status
            
            if user_status == False:
                username = raw_input("user:")
                password = raw_input("password:")
                if username == _username and password == _password:
                    print("welcome login....")
                    user_status = True
                else:
                    print ("wrong username or password!")        
            if user_status:
                func(*args,**kwargs)
        
        return inner
    return outer
    
        
        
def home():
    print "---首页---"
    
def america():
    print "---美国---"

def japan():
    print "---日本---"
#@login
@login('qq')   #beijing = login(beijing)   #@login等价于beijing = login(beijing)
               #login('qq')   1\login('qq')返回outer,然后变成@outer然后在执行的就是inner函数了
def beijing():
    print "---北京---"
    
#beijing = login(beijing)
ff = beijing('3q')
print ff


