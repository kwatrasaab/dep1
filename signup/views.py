from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import User
from .forms import SignupForm


# Create your views here.


def signup2(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SignupForm()
    return render(request, 'signup/signup.html', {'form': form})


def signup(request):
    return render(request, 'signup/index.html')


def registeruser(request):
    user = User()
    user.First_Name = request.POST.get('firstName')
    user.Last_Name = request.POST.get('lastName')
    user.Email = request.POST.get('email')
    user.Password = request.POST.get('password')
    user.Gender = request.POST.get('gender')
    user.DOB = str(request.POST.get('day') + '/' +
                   request.POST.get('month') + '/' +
                   request.POST.get('year'))
    user.save()
    return redirect('login/')
