from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(null=True, blank=True)
    bio = models.TextField(default="", blank=True)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    #def __str__(self):
    #    return self.user

class Post(models.Model):
    title = models.CharField(max_length=50, null=True)
    caption = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    userPosted = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=1000, null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    userPosted = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
