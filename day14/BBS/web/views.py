# -*- coding:utf-8 -*-

from django.shortcuts import render,render_to_response,HttpResponse
from web import models
from models import UserType,News,NewType,Chat,Admin,Reply
import common
import html_helper
import json 
from django.core import serializers 
#序列化django数据模块
# Create your views here.

def index(request,page):
    '''
        @分页展示
    '''
    all_data = models.News.objects.all().count()
    #return render_to_response('index.html',{'data':all_data})

    per_item =  int(request.COOKIES.get('pager_num',10))
    #获取cookie的传值    
    page = common.try_int(page, 1)
 
#     count = Host.objects.all().count()
#     #访问连接  http://127.0.0.1:8080/app/index/2


    pageobj = html_helper.PageInfo(page,all_data,per_item)
    start = pageobj.start
    stop = pageobj.end
    result = News.objects.all()[start:stop]
  
    all_pages = pageobj.all_pages
    Hpage = html_helper.pager(page,all_pages)
    
    ret = {'data':result,'count':all_data,'page':page,'Hpage':Hpage}
    response = render_to_response('index.html',ret)

    response.set_cookie('k1','v1')
    #设置cookie
    return response
 
 
    
def addfavor(request):
    '''
        @加赞
    '''
    ret = {'status':0,'data':'','message':''}
    
    try:
        id = request.POST.get('nid')
        print id
        newsObj = models.News.objects.get(id=id)    
        temp = newsObj.favor_count + 1
        newsObj.favor_count = temp
        newsObj.save()
        ret['status'] = 1
        ret['data'] = temp
    except Exception,e:
        ret['message'] = e.message
    
    return HttpResponse(json.dumps(ret))

def getreply(request):
    '''
        @评论
    '''
    id = request.POST.get('nid')
    #print id
    #reply_list = models.Reply.objects.filter(new__id=id).values('id','content','create_date','user__username')
    try:
        reply_list = models.Reply.objects.filter(new__id=id)
        reply_list = serializers.serialize("json",reply_list)
    #使用django的模块序列化数据
    except Exception,e:
         print e.message
    return HttpResponse(reply_list)
    #return HttpResponse(json.dumps(reply_list))
    #datetime.datetime(2017, 5, 31, 3, 27, 10, tzinfo=<UTC>)  时间格式是无法直接被json序列化的