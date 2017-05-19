# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
#导入跳转连接模块
from django.http.response import HttpResponse
#导入模块该模块可以加载处理html网页
from manager import models
from models import UserInfo
from models import Asset
from models import UserGroup
from forms import RegisterForm
from django.core.context_processors import request
#导入数据库模块

# Create your views here.


def register(request):
    register = RegisterForm()
    
    if request.method == 'POST':
    #判断是否是提交数据    
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print data
            
            #UserInfo.objects.create(
            #        username=request.POST.get('username'),
            #        password=request.POST.get('password'),
            #        email=request.POST.get('email'),
            #        typeId_id=request.POST.get('typeid'),)
            UserInfo.objects.create(
                    username=data['username'],
                    password=data['password'],
                    email=data['email'],
                    user_type_id=data['user_type_id'],)
        else:
            temp = form.errors.as_data()
            print temp['email'][0].messages[0]
    
    return render_to_response('register.html',{'form':register})
    
def login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)  
        #获取用户名  如果没有获取到赋值为None
        pwd = request.POST.get('password',None)
        #检查用户名和密码是否存在
        result = UserInfo.objects.filter(username=user,password=pwd).count()
        if result == 1:
            return redirect ('/manager/index/') 
            #登录成功跳转到首页
        else:
            return render_to_response('login.html',{'status':'用户名密码错误！'})
    else:
        return render_to_response('login.html')

def index(request):
        return render_to_response('index.html',{'status':'欢迎进入主机管理系统！'})

def host(request):
        return render_to_response('host.html',{'status':'添加主机'})
    
def add(request):
    if request.method == 'POST':
        hostname = request.POST.get('hostname',None) 
        ip = request.POST.get('ip',None) 
        groupname = request.POST.get('groupname',None)
        if hostname  and ip :
            Asset.objects.create(
                    hostname=hostname,
                    ip=ip,
                    user_group_id=groupname,)
            return redirect('/manager/list/')
        else:
            return render_to_response('host.html',{'decide':'主机信息输入有误，请重新输入！'})
    else:
        return render_to_response('host.html',{'status':'添加主机'})
    
def list(request):
    assert_list = Asset.objects.all()
    return render_to_response('assetlist.html',{'data':assert_list,'decide':'主机添加成功'})
    #上面的两行是输出所有的主机   
    
    #assert_list = Asset.objects.filter(user_group__GroupName='陨石地带') 
    #user_group__GroupName  选取是在models中定义的如下
    #user_group = models.ForeignKey('UserGroup')
    #return render_to_response('assetlist.html',{'data':assert_list,'decide':'主机添加成功'})
    #上面的两行使用的是跨表查询，user_group__GroupName跨表查询使用__  跨表取值使用的是.可以参考教程day12-02
        
def many(request):
    #处理多对多的情况   添加数据
    u1 = UserInfo.objects.get(id=2)
    #获取用户
    g1 = UserGroup.objects.get(id=3)
    #获取组
    g1.user.add(u1)
    #在多对多关系表中建立关系   user的选取是在models中定义的如下
    #user = models.ManyToManyField('UserInfo')
    #或是使用如下方式添加  u1.usergroup_set.add(g1)    注意两种方式u1和g1的顺序
    return HttpResponse('Ok')