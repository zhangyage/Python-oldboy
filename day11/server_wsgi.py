#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
使用wsgi编写的一个小型的web程序

可以插入断点查看一下environ,start_response变量的具体值
'''
from wsgiref.simple_server import make_server


def RunServer(environ,start_response):
    start_response('200 OK',[('content-Type','text/html')])
    return '<h1>hello,web1<h1>'

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print "serving HTTP on port 8000>>>"
    httpd.serve_forever()