from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index,addfavor,getreply,submitreply,login,logout,register,submitchat,getchat,getchat2

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^register/', register),  
    url(r'^index/(\d*)', index),
    url(r'^addfavor/', addfavor),
    url(r'^getreply/', getreply),
    url(r'^submitreply/', submitreply),
    url(r'^submitchat/', submitchat),
    url(r'^getchat/', getchat),
    url(r'^getchat2/', getchat2),
    
)
