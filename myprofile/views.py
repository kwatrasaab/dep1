from django.shortcuts import render, redirect
from signup.models import User


# Create your views here.


def red(request):
    return redirect('/login/')


def myprofile(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'myprofile/myprofile.html', {'user': user})
