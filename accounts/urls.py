"""Defines URL patterns for accounts"""

from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # Include default auth urls
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
    # Account Settings
    path('settings/', views.settings, name='settings'),
    # View friends list
    path('<str:username>/friends/', views.friends_list, name='friends_list'),
    # View pending friend requests
    path('friend_requests/', views.view_friend_requests, name='view_friend_requests'),
    # Send friend request
    path('send_friend_request/<str:sender_username>/<str:receiver_username>/', views.send_friend_request, name='send_friend_request'),
]