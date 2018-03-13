#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lxml import etree
import requests
import json
import sys

reload(sys)

sys.setdefaultencoding('utf-8')
def getsource(url):
    return requests.get(url)

urls = "http://mp.weixin.qq.com/s/9KAt4woK6BrrVKU4PY8dHg"

html = getsource(urls)
Selector = etree.HTML(html.text)
content_field = Selector.xpath('//*[@id="js_content"]/table/tbody/tr[@height="20"]')
item = {}
total = []
for each in content_field[1:]:
    project = each.xpath('td/span/text()')
#     print project[2]
    for i in project:
        print i
#     item['product'] = project[0]
#     item['start_time'] = project[1]
#     item['history_num'] = project[2]
#     item['new_nuw'] = project[3]
#     total.append(item)
# 
# print total     
# for i in total:
#     print i
    
