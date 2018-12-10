# from django.conf.urls import url
from django.urls import path
from .views import login as l1

app_name = 'login'

urlpatterns = [
    path('', l1, name='login'),
]
