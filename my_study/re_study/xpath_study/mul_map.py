#!/usr/bin/env python
# -*- coding:utf-8 -*-
#多线程爬虫

from multiprocessing.dummy import Pool as ThreadPool
import requests
import time
import get

def getsource(url):
    html = requests.get(url)
    
urls = []
for i in range(1,21):
    newpage = 'http://tieba.baidu.com/p/3522395718?pn=' +str(i)
    urls.append(newpage)
#print urls
time1 = time.time()
for i in urls:
    print i
    getsource(i)
time2 = time.time()
print u'单线程耗时' + str(time2-time1)


pool = ThreadPool(4)
#初始化实例
time3 = time.time()
results = pool.map(getsource,urls)
pool.close()
pool.join()
#等待爬去完成后再执行下面的内容
time4 = time.time()
print u'多线程耗时' + str(time4-time3)