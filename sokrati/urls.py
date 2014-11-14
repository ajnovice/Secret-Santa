from django.conf.urls import patterns, include, url
from secretfriends.views import friends

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sokrati.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', friends,name='friends'),
)
