#!/usr/bin/env python
# -*- coding:utf-8 -*-
#使用Python的nmap模块进行端口扫描

#执行的时候输入如下：www.vipysdd.com  22,80,443
#多主机的话：192.168.72.1,192.168.5.3 22,80,443

import sys
import nmap


scan_row = []
input_data = raw_input('Please input hosts and ports  :')
scan_row = input_data.split(" ")

if len(scan_row) !=2:
    print "Input error,example 192.168.1.2 80,443,22"
    sys.exit(0)

hosts = scan_row[0] #接受用户输入的主机
port = scan_row[1]  #接受用户收入的端口

try:
    nm = nmap.PortScanner()   #创建端口扫描对象
except nmap.PortScannerError:
#except Exception:
    print ('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print ('Unexcepted error', sys.exc_info()[0])
    sys.exit(0)

try:
    #调用主机扫描方法，参数指定扫描主机hosts,nmap扫描名两行参数arguements
    nm.scan(hosts=hosts,arguments=' -v -sS -p '+port)
except Exception,e:
    print "Scan error:" +str(e)

for host in nm.all_hosts():     #遍历扫描主机
    print('-------------------------------------------------------')
    print('Host: %s  (%s)' % (host,nm[host].hostname()))    #输出主机的ip和主机名
    print('Status: %s' % (nm[host].state()))                #输出主机的状态信息

for proto in nm[host].all_protocols():    #遍历扫描协议
    print('-------------------------------------------------------')
    print('Protocols: %s ' % proto)    #输出协议名

    lport = nm[host][proto].keys()    #获取协议的所有扫描端口
    lport.sort()        #端口列表排序
    for port in lport:  #遍历端口输出端口与状态
        print('port : %s\tstate : %s'%(port,nm[host][proto][port]['state']))
     