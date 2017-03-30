#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
在python文件中，如果我们要使用某个文件夹中的模块（py文件），这个文件必须是个包，及文件夹下面要有一个__init__的文件
'''

from day03 import demo        #导入模块

demo.FOO()
print 'index' ,__name__       #判断对应的文件是不是主文件
'''
def FOO():
    print "看到我了吧"
    print 'demo' ,__name__
当代码如上的情况时候，输出结果为：
看到我了吧
demo day03.demo         #通过木块导入的时候对应的__name__就是file.demo
index __main__
'''

if __name__ == "__main__":      #标准的入口程序都需要添加
    pass

print __file__                 #输出 D:\workspace\Python-oldboy\day03\index.py  
#输出当前文件的路径
print __doc__                  #输出在python文件中，如果我们要使用某个文件夹中的模块（py文件），这个文件必须是个包，及文件夹下面要有一个__init__的文件
#输出文件的注释
