# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect

# Create your views here.


from forms import Alogin


def index(request):
    obj = Alogin()    #实例化对象
    if request.method == 'POST':
    #判断请求类型
        checkForm = Alogin(request.POST)
        #获取传递的结果
        #print checkForm
        checkResult = checkForm.is_valid()
        #检测输入结果是否正确   是否符合制定的格式   这个比较有用可以判断输入格式避免了自己写正则表达式
        if checkResult:
            pass
        else:
            #errorObj = checkForm.errors
            #传递错误信息
            errorObj = checkForm.errors.as_data().values()[0][0].messages[0]
            #print errorObj
            #优化错误信息输出
        print checkResult
        #如果符合返回True   不符合返回False
    
    #return render_to_response('app01/index.html',{'data':obj,'status':errorObj})
    return render_to_response('app01/index.html',{'data':checkForm,'status':errorObj})
    #'data':obj和'data':checkForm的区别在于使用obj错误提交的时候表单内容内清空，  checkForm提示错误信息同时内容依然显示方便用户修改
    
