from django.conf.urls import include, url
import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'themostat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', 		 views.show_datepicker, name='datepicker'),
    url(r'^insert_tmp$', views.insert_tmp, name='tmp'),
    url(r'^onedaytmp$',  views.show_oneday_tmp, name='showtmp'),
  #  url(r'^show_lchart$',   views.show_linechart, name='showlchart'),
]

