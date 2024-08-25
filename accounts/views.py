from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import AccountUserForm
from .models import AccountUser

def register(request):
    """Register new user"""
    if request.method != 'POST':
        # Blank form
        form = UserCreationForm()
    else:
        # Process form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            AccountUser.objects.create(user=new_user)
            login(request, new_user)
            return redirect('social_media:index')
        
    # Display blank/invalid form
    return render(request, 'registration/register.html', {'form': form})

def settings(request):
    """Edit account settings"""
    account = get_object_or_404(AccountUser, user=request.user)
    
    if request.method != 'POST':
        form = AccountUserForm(instance=account)
    else:
        form = AccountUserForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            return redirect('social_media:profile', username=request.user.username)
        
    return render(request, 'registration/settings.html', {'form': form})