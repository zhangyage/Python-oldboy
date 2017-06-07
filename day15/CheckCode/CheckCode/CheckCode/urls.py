from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CheckCode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', views.Login),
    url(r'^checkcode', views.CheckCode),
)
