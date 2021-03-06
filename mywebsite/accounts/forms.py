from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Like, Profile

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'caption', 'image']

class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'text']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LikeForm(ModelForm):
    class Meta:
        model = Like
        fields = []
