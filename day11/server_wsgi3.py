#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
使用wsgi编写的一个小型的web程序

可以插入断点查看一下environ,start_response变量的具体值
升级版  根据访问的路径不同使用返回不同的网页，一个小型的路由系统
升级版2
'''
from wsgiref.simple_server import make_server


def RunServer(environ,start_response):
    start_response('200 OK',[('content-Type','text/html')])
    #获取url
    userUrl = environ['PATH_INFO']
    
    func = None
    
    for item in url:
        if item[0] == userUrl:
            func = item[1]
            break
    
    if not func:
        result = func()
    else:
        result = '<h1>404:您访问的页面不存在！</h1>'
    return result
            
            
def index():
    print 'index'
    
def login():
    print 'login'
    
def logout():
    print 'logout'
    
url = (('/index/','index'),
       ('/login/','login'),
       ('/logout/','logout'),)
    
if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "serving HTTP on port 8000>>>"
    httpd.serve_forever()