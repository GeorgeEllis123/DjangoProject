from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def profile(request, pk):
    profile = Profile.objects.get(user_id=pk)

    posts = profile.post_set.all()

    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'profile': profile, 'posts': posts, 'form': form}
    return render(request, 'accounts/profile.html', context)

def settings(request):
    return render(request, 'accounts/settings.html')

def feed(request):
    posts = Post.objects.all()
    return render(request, 'accounts/feed.html', {'posts': posts})

def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, 'accounts/register.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)

    comments = post.comment_set.all()

    form = CommentForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'post': post, 'comments': comments, 'form': form}
    return render(request, 'accounts/post.html', context)
