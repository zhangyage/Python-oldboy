# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import register,login,index,host,add,list


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'service_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', register),
    url(r'^login/', login),
    url(r'^index/', index),
    url(r'^host/', host),
    url(r'^add/', add),
    url(r'^list/', list),
)
