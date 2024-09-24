from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm
from .models import Profile, User, FriendRequest
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

@login_required
def view_friend_requests(request):
    """View pending friend requests"""
    friend_requests = FriendRequest.objects.filter(receiver=request.user, status=1)
    return render(request, 'registration/view_friend_requests.html', {'friend_requests': friend_requests})

def send_friend_request(request, sender_username, receiver_username):
    """Send friend request to another user"""
    send_user = get_object_or_404(User, username=sender_username)
    rec_user = get_object_or_404(User, username=receiver_username)
    friend_req = FriendRequest.objects.create(sender = send_user, receiver = rec_user)
    return redirect('social_media:profile', username=receiver_username)

def process_friend_request(request, request_id, action):
    """Accept or reject friend request"""
    friend_request = get_object_or_404(FriendRequest, id=request_id)

    if action == 'accept':
        friend_request.status = 2
        friend_request.save()
        
        sender = Profile.objects.get(owner=friend_request.sender)
        receiver = Profile.objects.get(owner=friend_request.receiver)
        sender.friends.add(receiver)
        receiver.friends.add(sender)

    elif action == 'reject':
        friend_request.status = 3
        friend_request.save()

    return redirect('accounts:view_friend_requests')
