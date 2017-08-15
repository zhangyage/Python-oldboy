#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
基于DNS的轮训检测
'''

import dns.resolver
import os
import httplib
from decimal import getcontext

iplist = []    #定义域名的IP列表      
appdomain="www.izzjr.com"   #定义业务域名

def get_iplist(domain=""):  #解析域名，解析的结果追加到iplist列表中
    try:
        A = dns.resolver.query(domain,'A')
    except Exception,e:
        print "dns resolver error:" +str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j)   #追加ip到列表中
    return True

def checkip(ip):
    ip = str(ip)
    checkurl=ip+":80"
    getcontent=""
    httplib.socket.setdefaulttimeout(5)  #定义http的链接超时时间
    conn=httplib.HTTPConnection(checkurl)  #创建http链接对象
    
    try:
        conn.request("GET","/",headers = {"Host":appdomain})  #发起请求，添加host主机头
        r=conn.getresponse()
        #print r.read(6)
        getcontent = r.read(6)   #获取URl页面的前15个字符，以便后期做校验
        print getcontent
        
    finally:
        if getcontent == "<html>":
            #print len(getcontent)
           # print len("<html>")
            print ip+ "[ OK]"
        else:
           # print len(getcontent)
           # print len("<html>")
            print ip+ "[ Error]"
            
if __name__ == "__main__":
    if get_iplist(appdomain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print "Dns resolver error."        