from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_study.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/(\d*)', index),
)
