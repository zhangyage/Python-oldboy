#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

f = open('text.txt','r')
html = f.read()
f.close()

#获取网页的标题
title = re.search('<title>(.*?)</title>', html,re.S).group(1)
print title
#注释： re.S是为了消除换行带来的影响  .group(1)获取正则表达式中第一个（）的元素，如果是group(2)就是获取第二个匹配的元素
#search和findall的区别在于search找到一个后就不在查找了，而findall会遍历整个文件进行查找
#因为我们的标题只有一个

#获取链接    原文中有四个链接这个时候我们就要使用findall
links = re.findall('href="(.*?)"', html, re.S)
#print links
for each in links:
    print each
    
#抓取部分内容  先抓大在抓小
text_filed = re.findall('<ul>(.*?)</ul>', html,re.S)[0]
#到我们使用search配合group使用  使用findall配合[0]使用
the_text = re.findall('">(.*?)</a>', text_filed,re.S)
for each in the_text:
    print each

old_url = 'http://zhangyage.com?pageNum=1'    
total_page = 20
#sub实现翻页操作    sub的作用是替换内容
for i in range(2,total_page+1):
    new_link = re.sub('pageNum=\d+', 'pageNum=%d' % i, old_url, re.S)
    print new_link


