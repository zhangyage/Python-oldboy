#!/usr/bin/env python
# -*- coding:utf-8 -*-

#通过使用正则表单是筛选出网页中列表的标题   这里我们测试需要，直接将网站的源码粘贴到了jike.txt中

import re


#读取网站代码：
f = open('jike.txt','r')
html = f.read()
f.close()

#匹配图片网址   #posColumn=2688.2">Python 类深入</a>
title = re.findall('<h2 class="lesson-info-h2">(.*?)posColumn=(.*?)">(.*?)</a>', html, re.S)
for each in title:
    print each[2]
# i = 0
# for each in pic_url:
#     print 'now downloding:' + each
#     pic = requests.get(each)
#     fp = open('pic\\' + str(i) + '.jpg' , 'wb')
#     fp.write(pic.content)
#     fp.close()
#     i = i+1