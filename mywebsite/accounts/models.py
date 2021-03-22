from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )

    bio = models.TextField(default="", blank=True)
    #profile_pic = asdf

    def __str__(self):
        return self.username

    # one-to-one relationship w/ User

class Post(models.Model):
    title = models.CharField(max_length=50, null=True)
    caption = models.CharField(max_length=200, null=True)
    #image = asdf
    post_date = models.DateTimeField('date published')
    #userPosted = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #comments = models.ForeignKey(Comment, on_delete=models.SET_NULL)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    # one-to-many relationship w/ comment model

class Comment(models.Model):
    title = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=1000, null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    # one-to-many relationship w/ User
    # one-to-many relationship w/ post model

# Create your models here.
