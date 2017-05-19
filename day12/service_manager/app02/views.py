# Create your views here.
# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse,render,render_to_response,redirect
import json


# Create your views here.

def ajax(request):
    if request.method == 'POST':
        print request.POST
        #获取网页的传递值  是个字典
        print request.POST.get('dat')
        #获取对应字典元素的value值
        #return HttpResponse('ok')
        
        dicttest = {'ip':'123.123.123.23','hostname':'yazhoujuejin','address':'beijing'} 
        return HttpResponse(json.dumps(dicttest))
        #将数据通过json的方式传递给前段展示
    else:
        return render_to_response('app02/index.html')