#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
编写一个程序，模仿sed的功能，让它有替换的效果
当输入  fang_sed.py  old_text new_text filename --bak 时候可以进行备份和相关字符的替换
'''

import sys,os

if len(sys.argv) <= 4:
    print "usage:./fang_sed.py old_text new_text filename --bak"
    
old_text,new_text = sys.argv[1],sys.argv[2]
filename = sys.argv[3]

f = file(filename,'rb')
new_file = file('.%s.bak' % filename,'wb')
for line in f.readlines():
    new_file.write(line.replace(old_text,new_text))
f.close()
new_file.close()

if '--bak' in sys.argv:
    os.rename(filename,'%s.bak' % filename)
    os.rename('.%s.bak' % filename,filename)
else:
    os.rename('.%s.bak' % filename,filename)
