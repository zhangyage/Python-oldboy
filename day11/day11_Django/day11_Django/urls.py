# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.views import index,login,list,pic,photo
import web.urls

#导入模块


#使用反射重新路由实现自动路由
def active(request):
    #1、获取url
    #2、获取app名字
    #3、获取文件名
    #4、获取函数
    pass


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'day11_Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', index),
    #自定义url 放访问连接后加入index可以跳转到index函数  index函数在views中定义
    url(r'^login/', login),
    url(r'^list/(\d*)', list),
    #(\d*)代表数字
    
 
    url(r'^pic/(?P<name>\d*)', pic),
    #使用模板方式定义参数  name就是我们定义的参数，我们在views中设置参数就必须使用name
    
    
    url(r'^photo/(?P<name>\d*)/(?P<id>\d*)/$', photo),
    url(r'^photo/(?P<name>\d*)/', photo,{'id':2000}),
    #上面两条规则制定url的跳转规则，如果url中有两个变量第一个值传递给name,第二个值传递为id
    #在访问的url中在添加一个字段字段的默认值是id数值为2000
    
    url(r'^web/', include(web.urls)),
     #url分级，当访问web时候使用web下面的urls处理   不同的访问前缀使用的app urls处理
    
    
    #url(r'^', active),
)
