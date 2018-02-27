#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

secret_code = 'dhajdahxxixxdhhdkajduiiwurwsbxxlovexxvnvb==jdrievnhuetkfakfvxxyouxxuATE2QURG'


#.的使用举例
a = 'xz123'
b = re.findall('x.',a)
print b
#输出结果 ['xz']  .代表匹配后面的一个字符

#*的使用举例
a = 'xxxxxxz1x2x3'
b = re.findall('x*',a)
print b
#输出结果 ['xxxxxx', '', '', 'x', '', 'x', '', '']  .代表匹配前面的字符一次或多次


#?的使用举例
a = 'xxxxxxz1x2x3'
b = re.findall('x?',a)
print b
#输出结果 ['x', 'x', 'x', 'x', 'x', 'x', '', '', 'x', '', 'x', '', '']  .代表匹配前面的字符零次或者一次

#上面的内容需要我们进行了解，需要我们掌握的是如下组合（。*?）
b = re.findall('xx.*xx',secret_code)
print b
#['xxixxdhhdkajduiiwurwsbxxlovexxvnvb==jdrievnhuetkfakfvxxyouxx']

b = re.findall('xx.*?xx',secret_code)
print b
#['xxixx', 'xxlovexx', 'xxyouxx']

b = re.findall('xx(.*?)xx',secret_code,re.S)
print b
#注释，re.S在使用.匹配的时候可以匹配换行符，就是换行的可以自动连接
#['i', 'love', 'you']


#匹配数字
a = '''sdsdsdadadc343fdfad2ada34343adcada222ds'''
b = re.findall('\d+', a)
print b
#['343', '2', '34343', '222']