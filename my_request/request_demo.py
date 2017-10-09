#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


URL_IP = "http://192.168.75.128:8000/ip"
URL_GET = "http://192.168.75.128:8000/get"
#本地搭建的httpbin的服务端

#简单请求
def use_simple_requests():
    #response = urllib2.urlopen(URL_IP)
    response = requests.get(URL_IP)
    #操作类似于本地打开网络文件
    
    print '>>>>>Response Headers:'
    print response.headers
    #获取头部信息
    print '>>>>>Response Body:'
    print response.text

#构建带有参数的请求：
def use_params_requests():
    #构建参数
    params = {'param1':'hello','param2':'world'}
    #发送请求   类似  URL_IP？params
    response = requests.get(URL_GET, params=params)
    #处理响应
    print '>>>>>Response Headers:'
    print response.headers
    print '>>>>>Status code:'
    print response.status_code
    print response.reason
    #reason解释为什么是200
    print '>>>>>Response Body:'
    print response.json()
      
    
    
if __name__ == '__main__':
    print '>>>>use_simple_urllib2'
    use_simple_requests()
    print
    print '>>>>Params'
    use_params_requests() 