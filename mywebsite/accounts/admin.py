from django.contrib import admin

# Register your models here.

from .models import Profile
from .models import Post
from .models import Comment


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
