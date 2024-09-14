"""Defines URL patterns for social_media"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'social_media'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # User page
    path('profile/<str:username>/', views.profile, name='profile'),
    # Create new post
    path('new_post/', views.new_post, name='new_post'),
    # View post
    path('posts/<int:post_id>/', views.post, name="post"),
    # Delete post
    path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    # Search
    path('search/', views.search, name='search'),
    # Create new comment
    path('posts/<int:post_id>/new_comment/', views.new_comment, name='new_comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)