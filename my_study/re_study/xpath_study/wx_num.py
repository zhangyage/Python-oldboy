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
for each in content_field[1:]:
    project = each.xpath('td/span/text()')
    for i in project:
        print i
    
