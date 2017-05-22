from django.conf.urls import patterns, include, url
from django.contrib import admin
import app.urls
import app02.urls
#from app.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_study.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include(app.urls)),
    url(r'^app02/', include(app02.urls)),
)
