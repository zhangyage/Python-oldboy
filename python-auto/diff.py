#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
使用在python2.3以后自带的difflib模块比较两个字符串的不同
'''
import difflib

text1='''text1:
Python 3.0 was released in 2008. The final 2.x version 2.7 release came out in mid-2010
with a statement of extended support for this end-of-life release.
difflib document v7.4
add string
'''
text1_lines = text1.splitlines()  #按照行为单位进行封

text2='''text2:
Python 3.0 was released in 2008. The final 2.x version 2.7 release came out in mid-2010
with a statement of extended support for this end-of-life release.
difflib document v7.5
'''
text2_lines = text2.splitlines()  #按照行为单位进行封
d = difflib.Differ()   #创建differ（）对象
diff = d.compare(text1_lines,text2_lines)  #使用compre方法进行字符串比较
print '\n'.join(list(diff))
