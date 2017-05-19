# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
import manager.urls
import app01.urls
import app02.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'service_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^manager/', include(manager.urls)),
    url(r'^app01/', include(app01.urls)),
    url(r'^app02/', include(app02.urls)),
    
)
