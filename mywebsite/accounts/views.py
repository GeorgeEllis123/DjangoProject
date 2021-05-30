# Imports from django
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Imports from my files
from .models import *
from .forms import *
from .decorators import unauthenticated_user
# ---------------------------------------------------------------------------- #

# Renders the home page
def home(request):
    currentUser = request.user
    context = {"user": currentUser}
    return render(request, 'accounts/home.html', context)


# Renders the profile page
def profile(request, pk):
    # Displays forms on profile page if it is the logged in user's profile page
    if int(pk) == request.user.id:
        form_post = PostForm() # Gets the form to add posts

        # Gets the forms to modify the user and their profile
        updateUser = User.objects.get(id=pk)
        form_user = UpdateUserForm(instance=updateUser) # Prefills form with user data
        profile = Profile.objects.get(user_id=pk)
        form_profile = UpdateProfileForm(instance=profile) # Prefills form with profile data

        # Checks if the view recieved post data from a form being submitted
        if request.method == "POST":
            formData = PostForm(request.POST) # Saves the post data

            if 'NewPost' in request.POST.keys(): # Checks if the create post form was submitted
                if formData.is_valid(): # Checks if the form was completed
                    # Saves the data
                    stock = form_post.save(commit=False)
                    stock.userPosted = request.user.profile
                    stock.save()

            # Saves the post data
            userData = UpdateUserForm(request.POST, instance=updateUser)
            profileData = UpdateProfileForm(request.POST, instance=profile)

            if 'Update' in request.POST.keys(): # Checks if the update user form was submitted
                if userData.is_valid(): # Checks if the form was completed
                    userData.save() # Saves the data

                if profileData.is_valid(): # Checks if the form was completed
                    profileData.save() # Saves the data

    else:
        # Makes it so no forms are sent to the profile page template
        form_post = None
        form_user = None
        form_profile = None

    # Gets the user's profile and all of their posts
    profile = Profile.objects.get(user_id=pk)
    posts = profile.post_set.all()

    # Sends all of the data to the profile template
    context = {'profile': profile, 'posts': posts, 'form_post': form_post, 'form_user': form_user, 'form_profile': form_profile}
    return render(request, 'accounts/profile.html', context)


# Renders the feed page
def feed(request):
    posts = Post.objects.all() # Gets all of the post models

    # Sends all of the data to the feed template
    context = {'posts': posts}
    return render(request, 'accounts/feed.html', context)


# Renders the login page
@unauthenticated_user # Makes sure the user is not logged in
def loginPage(request):
    # Checks if the view recieved post data from a form being submitted
    if request.method == "POST":
        # Saves the password and username from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Checks the users information
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Logs the user if user exists
            login(request, user)
            return redirect('home_page')
        else:
            # Displays and error message if user does not exist
            messages.info(request, 'Username OR Password is incorrect')

    return render(request, 'accounts/login.html')


# Logs out the user
def logoutUser(request):
    logout(request)
    return redirect('login_page') # Redirects the user to the login page


# Renders the register page
@unauthenticated_user # Makes sure the user is not logged in
def register(request):
    form = CreateUserForm() # Gets the form to create a new user

    # Checks if the view recieved post data from a form being submitted
    if request.method == 'POST':
        form = CreateUserForm(request.POST) # Saves the post data
        if form.is_valid(): # Checks if the form was completed
            # Saves the data
            form.save()
            user = form.cleaned_data.get('username')

            # Displays success message
            messages.success(request, 'Account was created for ' + user)

            return redirect('login_page') # Sends user to login page

    # Sends register form to the register template
    context = {"form": form}
    return render(request, 'accounts/register.html', context)


# Renders the post page (displays a single post and all its data)
def post(request, pk):
    post = Post.objects.get(id=pk) # Gets the post for the specific page
    comments = post.comment_set.all() # Gets all of the comments for the post
    likes = post.like_set.all() # Gets all of the likes for the post
    user = request.user # Gets the user

    form = CommentForm() # Gets the form to add comments

    # Checks if the user already liked the post
    LIKED = False
    for like in likes:
        if like.user.user == user:
            LIKED = True

    # Gets the like form only if the post has not already been liked
    if LIKED:
        form_like = None
    else:
        form_like = LikeForm()

    # Checks if the view recieved post data from a form being submitted
    if request.method == "POST":
        formData = CommentForm(request.POST) # Saves the post data
        if 'Comment' in request.POST.keys(): # Checks if the create comment form was submitted
            if formData.is_valid(): # Checks if the form was completed
                # Saves the data
                stock = formData.save(commit=False)
                stock.userPosted = request.user.profile
                stock.post = post

                stock.save()

        formData = LikeForm(request.POST) # Saves the post data
        if 'Like' in request.POST.keys(): # Checks if the add like form was submitted
            if formData.is_valid(): # Checks if the form was completed
                # Saves the data
                stock = formData.save(commit=False)
                stock.user = request.user.profile
                stock.liked_post = post
                post.likes += 1 # Adds a like to the post model

                stock.save()
                post.save()

    # Sends all of the data to the post template
    context = {'post': post, 'comments': comments, 'form': form, 'form_like': form_like}
    return render(request, 'accounts/post.html', context)


# Renders the liked posts page (diplays all of the user's like posts)
def likedposts(request, pk):
    # Sends user to their liked-posts page if it is their page
    if int(pk) == request.user.id:
        # Gets the user's profile and all of their likes
        profile = Profile.objects.get(user_id=pk)
        likes = profile.like_set.all()

        # Gets all of the posts from the user's like models
        posts = []
        for i in likes:
            posts.append(i.liked_post)

        # Sends all of the data to the liked posts template
        context = {'profile': profile, 'posts': posts}
        return render(request, 'accounts/liked.html', context)

    else:
        return redirect('home_page') # Redirects the user to the home page
