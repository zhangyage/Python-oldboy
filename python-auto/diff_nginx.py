#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
使用difflib模块比较nginx配置文件的不同

执行python diff_nginx.py pydns.py pydns2.py > pydns.html
'''

import difflib
import sys
from logging import FileHandler

try:
    textfile1 = sys.argv[1]  #配置文件1的路径
    textfile2 = sys.argv[2]  #配置文件2的路径
except Exception,e:
    print "Error:" +str(e)
    print "Usage:diff_nginx.py filename1 filename2"
    sys.exit()
    
def readfile(filename):   #文件读取的分割函数
    try:
        fileHandle = open (filename,'rb')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print ("Read file error" +str(error))
        sys.exit()
        
if textfile1=="" or textfile2=="":
    print "Usage:diff_nginx.py filename1 filename2"
    sys.exit()
    
text1_file = readfile(textfile1)   #调用文件处理函数
text2_file = readfile(textfile2)

d = difflib.HtmlDiff()   #创建differ（）对象
print d.make_file(text1_file,text2_file)

        