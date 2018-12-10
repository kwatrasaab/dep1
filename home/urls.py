# from django.conf.urls import url, path
from django.urls import re_path, path
from .views import home as h1

app_name = 'home'

urlpatterns = [
    # url('^$', views.home, name='home'),
    re_path(r'^(?P<user_id>[0-9]+)/$', h1, name='home'),
]
