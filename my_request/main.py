#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests
from requests import exceptions

URL = "https://api.github.com"

def build_uri(endpoint):
    '''
    @拼合连接
    '''
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)
    #indent 定制锁进为4


def request_methods():
    #response = requests.get(build_uri('users/zhangyage'))
    response = requests.get(build_uri('user/emails'),auth=('zhangyage','*****'))
    print better_print(response.text)
    
def params_request():
    response = requests.get(build_uri('users'),params={'since':11})
    print better_print(response.text)
    print response.request.headers
    print response.url
    

def timeout_resquest():
    '''
    @异常处理
    '''
    try:
        #response = requests.get(build_uri('user/emails'), timeout=0.1)
        response = requests.get(build_uri('user/emails'), timeout=5)
        response.raise_for_status()    #显示的处理异常
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    
    else:
        print response.text
        print response.status_code
        
def hard_request():
    '''
            @ 自定义request
    '''
    from requests import Request,Session
    s = Session()
    headers = {'User-Agent':'fake1.3.4'} 
    req = Request('GET',build_uri('user/emails'),auth=('zhangyage','*****'),headers=headers)
    prepped = req.prepare()   #准备
    print prepped.body
    print prepped.headers
    
    #开始发送
    resp = s.send(prepped,timeout=5)
    print resp.status_code
    print resp.request.headers
    print resp.text
    
    
    

if __name__ == '__main__':
    #request_methods()
    #params_request()
    #timeout_resquest()
    hard_request()
