from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from .forms import PostForm

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def profile(request, pk):
    profile = Profile.objects.get(user_id=pk)

    posts = profile.post_set.all()

    form = PostForm()

    context = {'profile': profile, 'posts':posts, 'form': form}
    return render(request, 'accounts/profile.html', context)

def settings(request):
    return render(request, 'accounts/settings.html')

def feed(request):
    posts = Post.objects.all()
    return render(request, 'accounts/feed.html', {'posts': posts})

def login(request):
    return render(request, 'accounts/login.html')
