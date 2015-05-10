from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'themostat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$',		  'views.index', name='index'),
    url(r'^', 		  include('themocheck.urls', namespace="themocheck")),
    url(r'^admin/', 	  include(admin.site.urls)),
]
