# -*- coding:utf-8 -*-
from django.shortcuts import render,HttpResponse,render_to_response,redirect
from django.template.context import RequestContext


# Create your views here.

def login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)  
        #获取用户名  如果没有获取到赋值为None
        pwd = request.POST.get('password',None)
        #检查用户名和密码是否存在
        if user == 'zhang' and pwd == '123':
            #request.session['is_login'] = True
            request.session['is_login'] = {'user':user}
            #定义一下session
            return redirect('/app02/index/')
        else:
            return render_to_response('app02/login.html',{'status':'用户名或密码错误'})
    
    return render_to_response('app02/login.html',context_instance=RequestContext(request))
    #context_instance=RequestContext(request)   tocken配合

def index(request):
    #is_login = request.session.get('is_login')
    user_dict = request.session.get('is_login',None)
    #获取session值
    if not user_dict:
        #print user_dict['user']
        #如果为空就跳转登录页面
        return redirect('/app02/login/')
    return render_to_response('app02/index.html',{'username':user_dict['user']})


def logout(request):
    del request.session['is_login']
    #删除session
    return render_to_response('app02/login.html')