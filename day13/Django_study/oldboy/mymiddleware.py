#!/usr/bin/env python
# -*- coding:utf-8 -*-
#自定义中间件    在Django中定义的中间件必须有下面的4个函数
#使用中间件时候需要现在setting中引用一下


from django.http.response import HttpResponse

class Day13Middleware(object):
    def process_request(self,request):
        print '1.process_quest'
        
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print '2.process_view'
        
    def process_exception(self,request,exception):
        #处理异常的，只有在出错的时候才会执行
        print '3.process_exception'
        
    def process_response(self,request,response):
        print '4.process_response'
        return response
    