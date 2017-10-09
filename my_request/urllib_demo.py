#!/usr/bin/env python
# -*- coding:utf-8 -*-


#使用urlib模拟访问自己的服务端
import urllib
import urllib2


URL_IP = "http://192.168.75.128:8000/get"
#本地搭建的httpbin的服务端

#简单请求
def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
    #操作类似于本地打开网络文件
    
    print '>>>>>Response Headers:'
    print response.info()
    #获取头部信息
    print '>>>>>Response Body:'
    print ''.join([line for line in response.readlines()])

#构建带有参数的请求：
def use_params_urllib2():
    #构建参数
    params = urllib.urlencode({'param1':'hello','param2':'world'})
    print '>>>>Request Params'
    print params
    #发送请求   类似  URL_IP？params
    response = urllib2.urlopen('?'.join([URL_IP,'%s']) % params)
    #处理响应
    print '>>>>>Response Headers:'
    print response.info()
    print '>>>>>Status code:'
    print response.getcode()
    print '>>>>>Response Body:'
    print ''.join([line for line in response.readlines()])
     
    
    
if __name__ == '__main__':
    print '>>>>use_simple_urllib2'
    use_simple_urllib2()
    print
    print '>>>>Params'
    use_params_urllib2() 