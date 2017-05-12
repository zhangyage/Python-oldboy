#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
使用wsgi编写的一个小型的web程序

可以插入断点查看一下environ,start_response变量的具体值
升级版  根据访问的路径不同使用返回不同的网页，一个小型的路由系统
'''
from wsgiref.simple_server import make_server


def RunServer(environ,start_response):
    start_response('200 OK',[('content-Type','text/html')])
    #获取url
    userUrl = environ['PATH_INFO']
    if userUrl == '/index/':
        return '<h1>index<h1>'
    elif userUrl == '/login/':
        return '<h1>login<h1>'
    elif userUrl == '/logout/':
        return '<h1>logout<h1>'
    else:
        return '<h1>404:您访问的页面不存在！</h1>'
if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "serving HTTP on port 8000>>>"
    httpd.serve_forever()