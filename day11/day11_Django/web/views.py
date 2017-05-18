# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import request
from django.http.response import HttpResponse

from models import Asset
from test.test_httplib import CERT_fakehostname
from web.models import UserInfo
from web.forms import RegisterForm

#导入要处理的表

# Create your views here.

def index(request):
    return HttpResponse('index')


def login(request):
    return HttpResponse('login')

def list(request,id):
    print id
    #id就是我们在url中传递的页数，名字可以任意写 ,如果是多个参数按照顺序写
    #url(r'^list/(\d*)', list),
    return HttpResponse('list')

def pic(request,name):
    print name
    #name是我们使用模板指定的参数名称，必须使用name作为参数传递
    #url(r'^pic/(?P<name>\d*)', pic),
    return HttpResponse('photo picture')


def photo(request,name,id):
    print name,id
    #name是我们使用模板指定的参数名称，必须使用name作为参数传递
    #url(r'^photo/(?P<name>\d*)/(?P<id>\d*)/$', photo),
    #url(r'^photo/(?P<name>\d*)/', photo,{'id':2000}),
    return HttpResponse('photo picture')

#通过url传递name 将name插入数据库Asset表中，上面我们已经导入了Asset表
def Add(request,name):
    Asset.objects.create(hostname=name)
    #插入数据
    #或操作函数一样，我们定义好函数操作数据库中，需要到urls中设置路由规则同时导入我们写的Add模块
    #url(r'^add/(?P<name>\d*)/', Add),
    #访问连接：http://127.0.0.1:8080/web/add/68080/
    return HttpResponse ('OK')

def Delete(request,id):
    Asset.objects.get(id=id).delete()
    #获取单条数据删除    通过id判断
    #或操作函数一样，我们定义好函数操作数据库中，需要到urls中设置路由规则同时导入我们写的Add模块
    #url(r'^delete/(?P<id>\d*)/', Delete),
    #访问连接：http://127.0.0.1:8080/web/delete/1/
    return HttpResponse ('OK')




def Update(request,id,hostname):
    #单条修改
    #访问连接：http://127.0.0.1:8080/web/update/2/guan23/
    obj = Asset.objects.get(id=id)
    #获取数据
    obj.hostname = hostname
    #修改数据 
    obj.save()
    #保存
    return HttpResponse ('OK')

def ManyUpdate(request,id,hostname):
    #多行修改    获取id〉1的修改hostname
    Asset.objects.filter(id__gt=id).update(hostname = hostname)
    #访问连接：http://127.0.0.1:8080/web/manyupdate/1/guan23/
    return HttpResponse ('OK')

    '''
def Get(request,hostname):

    #查询    hostname__contains = hostname类似模糊查询   支持正则表达式
    assetlist = Asset.objects.filter(hostname__contains = hostname)
    for item in assetlist:
        print item.id
    #访问连接：http://127.0.0.1:8080/web/get/guan23/
    #访问连接：http://127.0.0.1:8080/web/get/gu/
    '''
    
    '''
    alldata = Asset.objects.all()
    #获取表中的所有行
    #也可以使用如下的方式获得 alldata = Asset.objects.filter(id__gt=id)设置id的值为0
    '''
def Get(request):
    '''
    temp = Asset.objects.all()[0:2]
    #获取前两行
    for item in temp:
        print item.id
    #访问连接：http://127.0.0.1:8080/web/get
    return HttpResponse ('OK')
    '''
    
    '''
    temp = Asset.objects.all().order_by('-id')
    #-id代表的是逆序
    #按照id排序逆序输出
    for item in temp:
        print item.id 
    #访问连接：http://127.0.0.1:8080/web/get
    return HttpResponse ('OK')   
    '''
    temp = Asset.objects.all().values_list()    
    print temp
    print temp.query
    return HttpResponse ('OK') 
def Assetlist(request):
        assert_list = Asset.objects.all()
        resullt = render_to_response('assetlist.html',{'data':assert_list,'user':'zhangyage'})
        return resullt
        #导入模块render_to_response主要用来调用html文件
        #from django.shortcuts import render_to_response
        #这里我们需要在setting中设置一下模板存放的路径
        #TEMPLATE_DIRS = (
        #    os.path.join(BASE_DIR,'template'),    
        #    )
        #将相关数据反馈给字典中的key，然后key传递给网页经过网页模板处理输出
        
        #访问连接：http://127.0.0.1:8080/web/assetlist

def Login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)  
        #获取用户名  如果没有获取到赋值为None
        pwd = request.POST.get('password',None)
        #检查用户名和密码是否存在
        result = UserInfo.objects.filter(username=user,password=pwd).count()
        if result == 1:
            return HttpResponse ('登陆成功！') 
        else:
            return render_to_response('login.html',{'status':'用户名密码错误！'})
    else:
        return render_to_response('login.html')
    
def Register(request):
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
                    typeId_id=data['typeid'],)
        else:
            temp = form.errors.as_data()
            print temp['email'][0].messages[0]
    
    return render_to_response('register.html',{'form':register})
    #return render_to_response('register.html',{'form':register})
    
    
        