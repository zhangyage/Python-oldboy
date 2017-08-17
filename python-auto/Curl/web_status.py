#!/usr/bin/env python
# -*- coding:utf-8 -*-

#python -m pip install pycurl

import os 
import sys
import time
import pycurl
from pycurl import CONNECTTIMEOUT, NOPROGRESS, FORBID_REUSE, MAXREDIRS,\
    DNS_CACHE_TIMEOUT, WRITEHEADER, WRITEDATA, PRETRANSFER_TIME,\
    STARTTRANSFER_TIME, TOTAL_TIME, HTTP_CODE, SIZE_DOWNLOAD, HEADER,\
    HEADER_SIZE, SPEED_DOWNLOAD


URL="http://www.vipysdd.com"  #探测地址
c = pycurl.Curl()                  #创建一个curl对象
c.setopt(pycurl.URL,URL)         #定义请求的url常量
c.setopt(pycurl.CONNECTTIMEOUT,5) #定义请求链接的等待时间
c.setopt(pycurl.TIMEOUT,5)        #定义请求超时时间
c.setopt(pycurl.NOPROGRESS,1)     #屏蔽下载进度条
c.setopt(pycurl.FORBID_REUSE,1)   #完成交互后强制断开链接，不重用
c.setopt(pycurl.MAXREDIRS,1)      #指定http重定向的最大次数为1
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)#设置保存DNS的时间为30秒

#创建一个文件报存http的头部信息和网页内容
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"\content.txt","wb")
c.setopt(pycurl.WRITEHEADER,indexfile)  #将返回的http头部信息写到indexfile文件中
c.setopt(pycurl.WRITEDATA,indexfile)    #将返回的html内容重定向到indexfile文件中

try:
    c.perform()     #提交请求
except Exception,e:
    print "connection error:" +str(e)
    indexfile.close()
    c.close()
    sys.exit()
    
NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)       #获取DNS的解析时间
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)             #获取建立链接的时间
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)     #获取从建立链接到准备传输消息耗费的时间
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME) #获取从建立链接到传输开始消费的时间
TOTAL_TIME = c.getinfo(c.TOTAL_TIME)                 #获取传输的总时间
HTTP_CODE = c.getinfo(c.HTTP_CODE)                   #获取http状态码
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)           #获取下载数据包的大小
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)               #获取http的头部大小
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)         #获取平均的下载速度

#打印数据
print "HTTP状态码: %s" %(HTTP_CODE)
print "DNS解析时间: %.2f ms" %(NAMELOOKUP_TIME)
print "建立链接时间: %.2f ms" %(CONNECT_TIME)
print "准备传输时间: %.2f ms" %(PRETRANSFER_TIME)
print "传输开始时间: %.2f ms" %(STARTTRANSFER_TIME)
print "传输结束时间: %.2f ms" %(TOTAL_TIME)
print "下载数据包大小: %d bytes" %(SIZE_DOWNLOAD)
print "Http头部大小: %d bytes " %(HEADER_SIZE)
print "平均的下载速度: %d bytes/s" %(SPEED_DOWNLOAD)
indexfile.close()
c.close()
