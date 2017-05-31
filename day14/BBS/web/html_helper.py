#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.utils.safestring import mark_safe


class PageInfo:
    def __init__(self,page,count,per_item=5):
        #per_item=5 设置默认值为5
        self.Page = page
        self.Count = count
        self.Per_item = per_item
    
    @property    
    def start(self):
        return (self.Page-1)*self.Per_item
    
    @property
    def end(self):
        return self.Page*self.Per_item
    
    @property
    def all_pages(self):
        all_pages,yushu = divmod(self.Count,self.Per_item)
        #divmod(count,per_item)的得到结果是商，余数
        if yushu == 0:
            all_pages = all_pages
        else:
            all_pages = all_pages+1
        return all_pages
            
def pager(page,all_pages):
    page_html = []
    
    first_html = "<a href='/web/index/%d'>首页</a>" % (1,)
    page_html.append(first_html)
    
    if page <=1:
        prev_html = "<a href='#'>上一页</a>" 
    else:
        prev_html = "<a href='/web/index/%d'>上一页</a>" % (page-1,)
    page_html.append(prev_html)
    
    begin = page - 6
    end = page + 5
    
    if all_pages < 12:
         begin = 0
         end = all_pages
    else:
        if page < 6:
            begin = 0
            end = 11
        else:
            if page + 6 > all_pages:
                begin = page - 5
                end = all_pages
            else:
                begin = page - 6
                end = page + 5
                
    for i in range(begin,end):
        if page == i+1:
            a_html = "<a class='selected' href='/web/index/%d'>%d</a>" % (i+1,i+1)
        else:
            a_html = "<a href='/web/index/%d'>%d</a>" % (i+1,i+1)
        page_html.append(a_html)
    
    if page < all_pages:
        next_html = "<a href='/web/index/%d'>下一页</a>" % (page+1,)     
    else:
        next_html = "<a href='#'>下一页</a>"
    page_html.append(next_html)
        
    end_html = "<a href='/web/index/%d'>最后一页</a>" % (all_pages,)
    page_html.append(end_html)    
        
    Hpage =  mark_safe(''.join(page_html))
    #Hpage =  mark_safe("<a href='/app/index/1'>1</a>")
    #mark_safe  将字符串转化为html标签，方法倒入方法如下：
    #from django.utils.safestring import mark_safe
    return  Hpage   