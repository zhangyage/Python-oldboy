# -*- coding:utf-8 -*-

from django.shortcuts import render,HttpResponse


# Create your views here.
#定制一个装饰器在执行前执行一个函数在执行后执行一个函数
def Filter(before_func,after_func):
    def outer(main_func):
        def wrapper(request,*args,**kwargs):
            before_result = before_func(request,*args,**kwargs)
            if(before_result != None):
                return before_result;
            
            main_result = main_func(request,*args,**kwargs)
            if(main_result != None):
                return main_result;
            
            after_result = after_func(request,*args,**kwargs)
            if(after_result != None):
                return after_result;          
        return wrapper 
    return outer    


def before_index(request):
    print 'before'

def after_index(request):
    print 'after'
    
@Filter(before_index,after_index)    
def index(request):
    print 'index'
    return HttpResponse('index')
    
