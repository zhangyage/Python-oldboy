#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lxml import etree
html1 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>测试-特殊用法</title>
</head>
<body>
    <div id="test-1">需要的内容1</div>
    <div id="test-2">需要的内容2</div>
    <div id="testfault">需要的内容3</div>
</body>
</html>
'''
Selector = etree.HTML(html1)

#提取以相同的字符开头   starts-with(@属性名称,属性字符相同的部分)
content = Selector.xpath('//div[starts-with(@id,"test")]/text()')
#通过谷歌浏览器获取xpath的路径后，添加text()即可获得文本内容
for each in content:
    print each
    
#输出
'''
需要的内容1
需要的内容2
需要的内容3
'''    
    
html2='''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test3">
        我左青龙，
        <span id="tiger">
            右白虎，
            <ul>上朱雀，
                <li>下玄武。</li>
            </ul>老牛在当中，
        </span>龙头在胸口。
    </div>
</body>
</html>
'''

Selector = etree.HTML(html2)

#提取标签套标签   
content = Selector.xpath('//div[@id="test3"]/text()')
for each in content:
    print each
#输出
'''
我左青龙，
        
龙头在胸口
'''
#提取标签套标签   
content = Selector.xpath('//div[@id="test3"]')[0]
info = content.xpath('string(.)')
#_ElementUnicodeResult: \n        我左青龙，\n        \n            右白虎，\n            上朱雀，\n                下玄武。\n            老牛在当中，\n        龙头在胸口。\n    
#去掉了所有的网页标签元素
content_2 = info.replace('\n','').replace(' ','')
print content_2
    