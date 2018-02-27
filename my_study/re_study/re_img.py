#!/usr/bin/env python
# -*- coding:utf-8 -*-

#通过使用正则表单是筛选出网页中的图片链接下载图片到本地   这里我们测试需要，直接将网站的源码粘贴到了jike.txt中

import re
import requests

#读取网站代码：
f = open('jike.txt','r')
html = f.read()
f.close()

#匹配图片网址   #img src="https://a1.jikexueyuan.com/home/201604/28/3f10/57216b7d1ac79.jpg" class="lessonimg"
pic_url = re.findall('img src="(.*?)" class="lessonimg"', html, re.S)
#print pic_url
i = 0
for each in pic_url:
    print 'now downloding:' + each
    pic = requests.get(each)
    fp = open('pic\\' + str(i) + '.jpg' , 'wb')
    fp.write(pic.content)
    fp.close()
    i = i+1