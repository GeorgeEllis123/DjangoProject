from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('profile/', views.profile),
    path('settings/', views.settings),
    path('feed/', views.feed),
    path('login/', views.login),

]
