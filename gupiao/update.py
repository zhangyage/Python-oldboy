#!/usr/bin/env python
# -*- coding:utf-8 -*-

#通过新浪借口爬取个股数据
#对应借口 http://hq.sinajs.cn/list=sh600641
#数据类型var hq_str_sh600641="万业企业,14.040,14.070,14.430,14.550,13.950,14.420,14.430,12126841,173814467.000,15800,14.420,29500,14.410,21199,14.400,39200,14.390,37450,14.380,14600,14.430,86600,14.440,65711,14.450,74100,14.460,75700,14.470,2017-09-15,10:55:05,00";

import urllib2
import re
import datetime
from model.model import Gu_info

url = "http://hq.sinajs.cn/list=sh603067"

rep = urllib2.Request(url)

rep.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER")
rep.add_header("Host","hq.sinajs.cn")
rep.add_header("Referer","http://finance.sina.com.cn/realstock/company/sh603067/nc.shtml")
#这个是key：value的关系具体的值可以通过使用浏览器的开发者模式自行查找定义
#可以伪造头部的很多字段和值
resp = urllib2.urlopen(rep)

info = resp.read().decode('gbk')
#读取对象，定义输出字符为中文避免乱码

name = info.split(',')[0].split('\"')[1]
nums = info.encode('utf-8').split(',')[0]
num = int(re.findall(r'\d+',nums)[0])
#print  info.split(',')[0].re.complie('/.d')
price =  float(info.split(',')[3])

print price

if __name__ == "__main__":
    gupiao = Gu_info()
    gupiao.Insertdata(name, num , price,)
