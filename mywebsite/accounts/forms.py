from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
