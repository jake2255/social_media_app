from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    """Profile form"""
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']
        labels = {'bio': 'Account Bio', 'profile_pic': 'Account Picture'}
