from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """Create new post"""
    class Meta:
        model = Post
        fields = ['caption', 'image']
        labels = {'caption': 'Post Caption', 'image': 'Post Image'}
