# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response,HttpResponse,redirect
from web import models
from models import News,Chat,Admin,Reply
import common
import html_helper
import json 
#from django.core import serializers
#序列化django数据模块 
import datetime
from datetime import date
from django.template.context import RequestContext



# Create your views here.
#定义一个装饰器验证用户的
def checklogin(main_func,*args,**kwargs):
    def wrapper(request):
        if request.session.get('is_login'):
            return main_func(request,*args,**kwargs)
        else:
            redirect('/web/login/')
    return wrapper


# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)  
        #获取用户名  如果没有获取到赋值为None
        pwd = request.POST.get('password',None)
        #检查用户名和密码是否存在
        result = Admin.objects.filter(username=user,password=pwd).count()
        if result == 1:
            #request.session['is_login'] = True
            request.session['is_login'] = {'user':user}
            #定义一下session
            return redirect('/web/index/')
        else:
            return render_to_response('login.html',{'status':'用户名或密码错误'})
    
    return render_to_response('login.html',context_instance=RequestContext(request))
    #context_instance=RequestContext(request)   tocken配合


def register(request):
    username = request.POST.get('username',None) 
    password = request.POST.get('password',None) 
    email = request.POST.get('email',None)
    user_type = request.POST.get('user_type',None)
    if request.method == 'POST':
        Admin.objects.create(username=username,password=password,email=email,user_type=user_type,)

    return render_to_response('register.html')


#@checklogin
def index(request,page):
    '''
        @分页展示
    '''
    all_data = models.News.objects.all().count()
    #return render_to_response('index.html',{'data':all_data})

    per_item =  int(request.COOKIES.get('pager_num',10))
    #获取cookie的传值    
    page = common.try_int(page, 1)
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


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self,obj)

def getreply(request):
    '''
        @评论
    '''
    id = request.POST.get('nid') 
    try:
        reply_list = models.Reply.objects.filter(new__id=id).values('id','content','create_date','user__username')
        reply_list = list(reply_list)
        #将django的数据类型转化为py的列表形
        reply_list = json.dumps(reply_list,cls=CJsonEncoder)
        #reply_list = serializers.serialize("json",reply_list)
    #使用django的模块序列化数据
    except Exception,e:
         print e.message
    return HttpResponse(reply_list)
    #return HttpResponse(json.dumps(reply_list))
    #datetime.datetime(2017, 5, 31, 3, 27, 10, tzinfo=<UTC>)  时间格式是无法直接被json序列化的
    
def submitreply(request):
    '''
        @提交评论内容
    '''
    id = request.POST.get('nid')
    data = request.POST.get('data')
    print id,data
    #models.Reply.objects.create(content=data,user=models.,new=models.News.objects.get(id=id),)