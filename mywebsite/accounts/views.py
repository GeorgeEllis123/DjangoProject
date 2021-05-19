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

def profile(request, pk):
    # Displays forms on profile page if the it is the logged in user's profile
    if int(pk) == request.user.id:
        form_post = PostForm()
        profile = Profile.objects.get(user_id=pk)
        form_profile = UpdateForm(instance=profile)
        if request.method == "POST":
            formData = PostForm(request.POST)
            if 'NewPost' in request.POST.keys():
                if formData.is_valid():
                    stock = form_post.save(commit=False)
                    stock.userPosted = request.user.profile
                    stock.save()
            formData = UpdateForm(request.POST, instance=profile)
            if 'Update' in request.POST.keys():
                if formData.is_valid():
                    formData.save()

    else:
        form_post = None
        form_profile = None

    profile = Profile.objects.get(user_id=pk)
    posts = profile.post_set.all()


    context = {'profile': profile, 'posts': posts, 'form_post': form_post, 'form_profile': form_profile}
    return render(request, 'accounts/profile.html', context)

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
    form_like = LikeForm()
    if request.method == "POST":
        formData = CommentForm(request.POST)
        if 'Comment' in request.POST.keys():
            if formData.is_valid():
                stock = formData.save(commit=False)
                stock.userPosted = request.user.profile
                stock.post = post
                stock.save()
        formData = LikeForm(request.POST)
        if 'Like' in request.POST.keys():
            if formData.is_valid():
                stock = formData.save(commit=False)
                stock.user = request.user.profile
                stock.liked_post = post
                post.likes += 1
                stock.save()
                post.save()

    context = {'post': post, 'comments': comments, 'form': form, 'form_like': form_like}
    return render(request, 'accounts/post.html', context)

def likedposts(request, pk):
    if int(pk) == request.user.id:
        profile = Profile.objects.get(user_id=pk)
        likes = profile.like_set.all()
        posts = []
        for i in likes:
            posts.append(i.liked_post)

        context = {'profile': profile, 'posts': posts}
        return render(request, 'accounts/liked.html', context)
    else:
        return redirect('home_page')
