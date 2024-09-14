from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    """Create new post"""
    class Meta:
        model = Post
        fields = ['caption', 'image']
        labels = {'caption': 'Post Caption', 'image': 'Post Image'}

class CommentForm(forms.ModelForm):
    """Create new comment"""
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'comment': 'New Comment'}

