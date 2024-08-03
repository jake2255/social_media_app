from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """Create new post"""
    class Meta:
        model = Post
        fields = ['text']
        labels = {}
