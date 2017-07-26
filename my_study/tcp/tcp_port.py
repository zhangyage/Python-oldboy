#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
核实服务器中开放的tcp端口
'''

import os
import json
from test.test_sys_setprofile import ident

data = {}
tcp_list = []
port_list = []
#windows下查看监听tcp端口的监听状况
command = 'netstat -ano -p tcp | find "LISTENING"'
lines = os.popen(command).readlines()
#将端口号过滤出追加到列表中port_list
for line in lines:
    port = line.split()[1].split(':')[1]
    port_list.append(port)
    
for port in list(set(port_list)):
    #set(port_list) set集合  集合是不让有重复元素的，这个方式数过滤列表的重复元素
    port_dict = {}
    port_dict['{#TCP_PORT}'] = port
    tcp_list.append(port_dict)
    
data['data'] = tcp_list
jsonStr = json.dumps(data, sort_keys=True,indent=4)
print jsonStr