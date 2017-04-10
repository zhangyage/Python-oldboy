#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
正则表达式的学习
尝试用的几个方法
match()
search()
group()
findall()
compile()
groups()
'''

import re


#re.match(pattern, string, flags)
#pattern  你要写的正则表达式
#string   你要匹配的字符串
#match和search的区别
reslut1 = re.match('\d+','123asf297a57a5a743894a0e4a801fc3')
print reslut1
print reslut1.group()
#输出123

reslut2 = re.search('\d+','asf297a57a5a743894a0e4a801fc3')
print reslut2
print reslut2.group()
#输出297

#match和search的共同点是，他们直接输出的结果都是一个对象，<_sre.SRE_Match object at 0x0000000001CC4578>，需要配合group输出，一个主意的点是他们只拿一个
#match和search的区别在于match是从开头匹配输出，如果没有就输出None不在输出对象所以在group输出是也是会报错的，search则是匹配整个字符串只要有就可以输出

reslut3 = re.findall('\d+','12358sdfeasf297a57a5a743894a0e4a801fc3')
print reslut3
#输出['12358', '297', '57', '5', '743894', '0', '4', '801', '3']
#findall可以上两个的区别在于，findall会查找全部匹配的并且安装列表的方式输出


#compile()使用方法
com = re.compile('\d+')
print com.findall('12358sdfeasf297a57a5a743894a0e4a801fc3')
#输出['12358', '297', '57', '5', '743894', '0', '4', '801', '3']
#当多个字符串的时候，使用compile()编译，可以提高效率


#groups()使用方法
#\d 数字 + 是>=1  \w代表_字母数字和-  *代表0个或多个重复
reslut4 = re.search('(\d+)\w*(\d+)','asf297a57a5a743894a0e4a801fc3')
print reslut4.group()
print reslut4.groups()
#输出297a57a5a743894a0e4a801fc3             ('297', '3')
#（\d+）代表分组，group代表获取所有   groups代表获取分组元素



#\d 数字  +代表>=1  \w代表_字母数字和-  *代表0个或多个重复
#\t制表符   .代表除了回车意外的所有字符
#*代表>=0   +代表>=1  ?代表0|1 {m}代表次数  {m,n}代表范围包括m也包括n
reslut4 = re.search('a{3,5}','aaaaaaaaaa')
print reslut4.group()
#输出aaaaa

#实例匹配一个正确的ip地址
reslut4 = re.search('[0-9]{1,3}(?:\.\d+){3}','12.56.32.hkjdfjsdhfjsdhkj.12.12.dlakjdlajdla12.23.45.56jhjdlajdlkajld')
print reslut4.group()
#?:是让后面相同的元素连接起来