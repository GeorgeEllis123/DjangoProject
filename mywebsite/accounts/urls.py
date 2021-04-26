from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('profile/<str:pk>/', views.profile, name="profile_page"),
    path('settings/', views.settings, name="settings_page"),
    path('feed/', views.feed, name="feed_page"),
    path('login/', views.login, name="login_page"),

]
