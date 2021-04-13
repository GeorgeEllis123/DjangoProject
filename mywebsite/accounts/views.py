from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def settings(request):
    return render(request, 'accounts/settings.html')

def feed(request):
    posts = Post.objects.all()
    return render(request, 'accounts/feed.html', {'posts': posts})

def login(request):
    return render(request, 'accounts/login.html')
