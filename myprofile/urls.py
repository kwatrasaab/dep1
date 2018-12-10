# from django.conf.urls import url
from django.urls import re_path, path
from .views import myprofile as mp1, red

app_name = 'myprofile'

urlpatterns = [
    # url('^$', views.myprofile, name='myprofile'),
    re_path(r'^(?P<user_id>[0-9]+)/$', mp1, name='myprofile'),
    path('login/', red, name='red'),
]
