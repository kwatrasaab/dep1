# from django.conf.urls import url
from django.urls import path
from .views import signup2 as su1, registeruser as ru1

app_name = 'signup'

urlpatterns = [
    path('', su1, name='signup'),
    path('login/', ru1, name='registeruser'),
]
