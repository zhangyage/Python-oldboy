# -*- coding:utf-8 -*-
from django.shortcuts import render,HttpResponse,render_to_response,redirect
from django.utils.safestring import mark_safe
from models import Host
import common
import html_helper
#from django import forms.Form 

# Create your views here.


def index(request,page):
    #result = Host.objects.all()
    #count = Host.objects.all().count()
    #输出全部内容

    #result = Host.objects.all()[0:5]
    #count = Host.objects.all()[0:5].count()
    #输出制定条数
    
     
    #print page

#     try:
#         page = int(page)
#         #将字符串转化为数字型
#     except Exception,e:
#         page = 1
#         print e    #异常报错输出
#             # 这段代码写在了common.py中作为公共部分使用

    page = common.try_int(page, 1)
    #调用公共异常处理设置默认值
#     per_item = 20
#     #定制一下每页的条目数
#     start = (page-1)*per_item 
#     stop = page*per_item
#     #设定开始和结束的位置
#     result = Host.objects.all()[start:stop]
    count = Host.objects.all().count()
    #访问连接  http://127.0.0.1:8080/app/index/2
    
#     all_pages,yushu = divmod(count,per_item)
#     #divmod(count,per_item)的得到结果是商，余数
#     if yushu == 0:
#         all_pages = all_pages
#     else:
#         all_pages = all_pages+1

    pageobj = html_helper.PageInfo(page,count,10)
    start = pageobj.start
    stop = pageobj.end
    result = Host.objects.all()[start:stop]
    
    
    all_pages = pageobj.all_pages
    Hpage = html_helper.pager(page,all_pages)
    
#     page_html = []
#     
#     first_html = "<a href='/app/index/%d'>首页</a>" % (1,)
#     page_html.append(first_html)
#     
#     if page <=1:
#         prev_html = "<a href='#'>上一页</a>" 
#     else:
#         prev_html = "<a href='/app/index/%d'>上一页</a>" % (page-1,)
#     page_html.append(prev_html)
#     
#     for i in range(all_pages):
#         if page == i+1:
#             a_html = "<a class='selected' href='/app/index/%d'>%d</a>" % (i+1,i+1)
#         else:
#             a_html = "<a href='/app/index/%d'>%d</a>" % (i+1,i+1)
#         page_html.append(a_html)
#     
#     next_html = "<a href='/app/index/%d'>下一页</a>" % (page+1,)
#     page_html.append(next_html)
#         
#     end_html = "<a href='/app/index/%d'>最后一页</a>" % (all_pages,)
#     page_html.append(end_html)    
#         
#     Hpage =  mark_safe(''.join(page_html))
#     #Hpage =  mark_safe("<a href='/app/index/1'>1</a>")
#     #mark_safe  将字符串转化为html标签，方法倒入方法如下：
#     #from django.utils.safestring import mark_safe
    
    
    ret = {'data':result,'count':count,'page':page,'Hpage':Hpage}
    return render_to_response('app/index.html',ret)
