from django.shortcuts import render
from signup.models import User


# Create your views here.


def home(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'home/home.html', {'user': user})
