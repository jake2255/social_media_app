"""Defines URL patterns for social_media"""

from django.urls import path
from . import views

app_name = 'social_media'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # User page
    path('user/', views.user_posts, name='user_posts'),
]