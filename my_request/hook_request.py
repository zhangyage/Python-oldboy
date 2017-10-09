#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


def get_key_info(response,*args,**kwargs):
    '''回调函数
    '''
    print response.headers['Content-Type']
    
def main():
    '''主程序
    '''
    requests.get("https://www.baidu.com", hooks=dict(response=get_key_info))

if "__name__" == "__main__":
    main()