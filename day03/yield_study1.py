#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
生成器函数  使用生成器函数编写一个xreaflines程序
'''


def Axreadlines():
    seek = 0
    while True:
        with open(u'学习笔记','r') as f:
            f.seek(seek)              #跳转指针到上次读的位置
            data = f.readline()
            if data:
                seek = f.tell()        #记录一下文件的位置
                yield data
            else:
                return                 #return函数中看见return函数就结束了


if __name__ == "__main__":
    for item in Axreadlines():
        print item