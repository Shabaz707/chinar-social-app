# F:\chinar\core\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('like_post/', views.like_post, name='like_post'), # <--- Add this line
]