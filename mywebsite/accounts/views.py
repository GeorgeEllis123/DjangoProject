#Imports from django
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#Imports from my files
from .models import *
from .forms import *
from .decorators import unauthenticated_user


def home(request):
    currentUser = request.user
    context = {"user": currentUser}
    return render(request, 'accounts/home.html', context)

@login_required(login_url='login_page')
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
    context = {}
    return render(request, 'accounts/settings.html')

def feed(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'accounts/feed.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    return render(request, 'accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login_page')

@unauthenticated_user
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login_page')


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
