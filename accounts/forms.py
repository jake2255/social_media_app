from django import forms
from .models import AccountUser

class AccountUserForm(forms.ModelForm):
    """Account user info"""
    class Meta:
        model = AccountUser
        fields = ['bio', 'profile_pic']
        labels = {'bio': 'Account Bio', 'profile_pic': 'Account Picture'}
