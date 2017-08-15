#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
python -m pip install dnspython
安装dns模块，可以帮助我们解析A MX CNAME NS等记录
'''
import dns.resolver

domain = raw_input('Plaese input an domain:')   #输入域名
A = dns.resolver.query(domain,'A')              #指定对应的查询类型  解析其他查询类型的话，只需要修改为对应的类型
for i in A.response.answer:
    for j in i.items:
        print j