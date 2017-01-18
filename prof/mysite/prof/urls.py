from django.conf.urls import url

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # This is the URL for the index page.
    url(r'^$', views.index, name='index'),
    # This is the URL for viewing classes
    url(r'^class/(?P<class_id>[0-9]+)/$', views.classDetails, name='Class Details'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page:': 'login/'}, name='logout'),
    #url(r'^changeattendance/$', views.get_attendance, name='Change Attendance')
]
