from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def profile(request):
    return render(request, 'accounts/profile.html')

def settings(request):
    return render(request, 'accounts/settings.html')

def feed(request):
    return render(request, 'accounts/feed.html')
