from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = PostForm
        fields = '__all__'
