#!/usr/bin/env python
# -*- coding:utf-8 -*-

import filecmp

a = "D:\workspace\Python-oldboy\python-auto\style"
b = "D:\workspace\Python-oldboy\python-auto\style2"

dirobj = filecmp.dircmp(a,b,['g_style.css'])   #比较两个目录，其中忽略g_style.css文件

#print dirobj.report()     #比较当前指定目录中的内容
#print dirobj.report_partial_closure()   #比较当前目录已经第一级目录的内容
#print dirobj.report_full_closure()      #递归目录比较
#print "left_list:" +str(dirobj.left_list) #做目录中的文件
#print "right_list:" +str(dirobj.right_list)    #有目录中的文件
print "common:" +str(dirobj.common)   #两遍目录共同存在的文件或是目录
print "left_only" + str(dirobj.left_only)  #只有做目录中存在的文件
print "right_only" + str(dirobj.right_only) #只有右目录中存在的文件
print "common_dirs" + str(dirobj.common_dirs) #存在的共同目录
print "common_files" + str(dirobj.common_files) #存在的共同文件
print "diff_files:" + str(dirobj.diff_files)