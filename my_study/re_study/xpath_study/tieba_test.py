#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lxml import etree
import requests
import json
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

f = open('content.txt','a')

def towrite(contentdict):
    f.writelines(u'回帖时间:' + str(contentdict['topic_reply_time']) + '\n')
    #f.writelines(u'回帖内容:' + unicode(contentdict['topic_reply_content']) + '\n')
    f.writelines(u'回帖人:' + contentdict['user_name'] + '\n\n')

def getsource(url):
    return requests.get(url)

urls = "http://tieba.baidu.com/p/3522395718?pn=1"

html = getsource(urls)
Selector = etree.HTML(html.text)
content_field = Selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
item = {}

for each in content_field:
    reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot',''))
    author = reply_info['author']['user_name']
    content = each.xpath('div[@class="d_post_content_main d_post_content_firstfloor"]/div[0]/cc/div[@class="d_post_content j_d_post_content "]/text()')
    reply_time = reply_info['content']['date']
    #print content
#     for i in content:
#         print i
    print reply_time
    print author
    #item['topic_reply_content'] = "content"
    item['user_name'] = author
    item['topic_reply_time'] = reply_time
    #print item
    towrite(item)