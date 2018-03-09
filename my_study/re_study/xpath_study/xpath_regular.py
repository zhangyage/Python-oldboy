#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lxml import etree
html = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>测试-常规用法</title>
</head>
<body>
<div id="content">
    <ul id="useful">
        <li>这是第一条信息</li>
        <li>这是第二条信息</li>
        <li>这是第三条信息</li>
    </ul>
    <ul id="useless">
        <li>不需要的信息1</li>
        <li>不需要的信息2</li>
        <li>不需要的信息3</li>
    </ul>

    <div id="url">
        <a href="http://jikexueyuan.com">极客学院</a>
        <a href="http://jikexueyuan.com/course/" title="极客学院课程库">点我打开课程库</a>
    </div>
</div>

</body>
</html>
'''
Selector = etree.HTML(html)

#提取文本
content = Selector.xpath('//ul[@id="useful"]/li/text()')[2]
#通过谷歌浏览器获取xpath的路径后，添加text()即可获得文本内容
print content
# for each in content:
#     print each
#输出
'''
这是第一条信息
这是第二条信息
这是第三条信息
'''
    
#提取属性
link = Selector.xpath('//a/@href')
for each in link:
    print each
#输出
'''
http://jikexueyuan.com
http://jikexueyuan.com/course/
'''
    
title = Selector.xpath('//a/@title')
print title[0]
#输出
'''
极客学院课程库
'''

#输出标题
title = Selector.xpath('//title/text()')
print title[0]
#输出
'''
测试-常规用法
'''