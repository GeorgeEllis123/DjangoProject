from django.urls import path
from . import views

# All my url paths for views
urlpatterns = [
    path('', views.home, name="home_page"),

    path('feed/', views.feed, name="feed_page"),
    path('login/', views.loginPage, name="login_page"),
    path('logout/',  views.logoutUser, name="logout"),
    path('register/', views.register, name="register_page"),

    path('delete/<str:pk>/', views.delete, name="delete_page"),
    path('likedposts/<str:pk>/', views.likedposts, name="likedposts_page"),
    path('profile/<str:pk>/', views.profile, name="profile_page"),
    path('post/<str:pk>/', views.post, name="post_page"),

]
