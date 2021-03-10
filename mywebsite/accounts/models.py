from django.db import models

class Profile(models.Model):
    #first_name = models.CharField(max_length=30, null=True)
    #last_name = models.CharField(max_length=30, null=True)
    #password = models.CharField(max_length=30, null=True)
    #email = models.CharField(max_length=100, null=True)
    #date_created = models.DateTimeField(auto_now_add=True, null=True)
    #all above info in user model
    
    username = models.CharField(max_length=30, null=True)
    bio = models.CharField(max_length=500, null=True)
    #profile_pic = asdf
    
    def __str__(self):
        return self.username
    
    # one-to-many relationship w/ post model
    # one-to-many relationship w/ comment model
    
class Post(models.Model):
    title = models.CharField(max_length=30, null=True)
    caption = models.CharField(max_length=200, null=True)
    #image = asdf
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    
    # one-to-many relationship w/ profile model
    # one-to-many relationship w/ comment model
    
class Comment(models.Model):
    title = models.CharField(max_length=30, null=True)
    text = models.CharField(max_length=1000, null=True)
    post_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title
    
    # one-to-many relationship w/ profile model
    # one-to-many relationship w/ post model

# Create your models here.
