#!/usr/bin/env python
# -*- coding:utf-8 -*-

def login(username):
    if username == 'zhang':
        return '登录成功'
    else:
        return '登录失败'
    
def detail():
    print '恭喜你获得丰厚奖金'
    
if __name__ == "__main__":
    user = raw_input('Please input your name:')
    reslut = login(user)
    if reslut == '登录成功':
        detail()
    else:
        print "your are fire!"