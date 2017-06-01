from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index,addfavor,getreply,submitreply,login

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login),
    url(r'^index/(\d*)', index),
    url(r'^addfavor/', addfavor),
    url(r'^getreply/', getreply),
    url(r'^submitreply/', submitreply),
    
)
