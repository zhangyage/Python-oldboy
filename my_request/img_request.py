#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

def download_img():
    '''
    @下载图片
    '''
    url = "https://www.jcd6.com/Public/Home/new/images/process_03.png"
    response = requests.get(url,stream=True)
    with open('demo.png','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
    
if __name__ == '__main__':
    download_img()