from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import login,index,logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_study.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login),
    url(r'^index/', index),
    url(r'^logout/', logout),
)
