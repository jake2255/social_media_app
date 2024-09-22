from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile, User
from django.contrib.auth.decorators import login_required

def register(request):
    """Register new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(owner=new_user)
            login(request, new_user)
            return redirect('social_media:index')
    return render(request, 'registration/register.html', {'form': form})

@login_required
def settings(request):
    """Edit profile settings"""
    profile = get_object_or_404(Profile, owner=request.user)
    
    if request.method != 'POST':
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('social_media:profile', username=request.user.username)
    return render(request, 'registration/settings.html', {'form': form})

@login_required
def friends_list(request, username):
    """Show friends list"""
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, owner=user)
    friends = profile.friends.all()
    return render(request, 'registration/friends_list.html', {'friends': friends})