#!/usr/bin/env python
# -*- coding:utf-8 -*-


def login(username):
    if username == 'zhang':
        print "登录成功！"
    else:
        print "登录失败！"
        
if __name__ == "__main__":
    user = raw_input("Please input your name:")
    login(user)