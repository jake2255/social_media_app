from django.shortcuts import render, redirect, get_object_or_404
from social_media.models import Post
from django.http import Http404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from accounts.models import AccountUser
from django.contrib.auth.models import User

def index(request):
    """Home page of site"""
    if request.user.is_authenticated:
        username = request.user.username
        feed = Post.objects.exclude(owner=request.user).order_by('created_on').reverse()
    else:
        username = None
        feed = None
    context = {
        'username': username,
        'feed': feed,
    }
    return render(request, 'social_media/index.html', context)

@login_required
def profile(request, username):
    """Show user profile"""
    user_name = get_object_or_404(User, username=username)
    posts = Post.objects.filter(owner=user_name).order_by('created_on')
    info = get_object_or_404(AccountUser, user=user_name)
    context = {
        'user_name': user_name,
        'posts': posts,
        'info': info,
    }
    if posts is not None:
        return render(request, 'social_media/profile.html', context)
    else:
        raise Http404('User profile does not exist')
    
@login_required
def new_post(request):
    """Create a new post"""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('social_media:profile', username=request.user.username)
    return render(request, 'social_media/new_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    """Delete a post"""
    post = Post.objects.get(pk=post_id)
    if request.method != 'POST':
        post.delete()
    return redirect('social_media:profile', username=request.user.username)
    
@login_required    
def post(request, post_id):
    """Show a post from user"""
    post = get_object_or_404(Post, pk=post_id)
    owner_username = post.owner.username
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    context = {
        'post': post,
        'username': username,
        'owner_username': owner_username,
    }
    return render(request, 'social_media/post.html', context)

def search(request):
    """Search for other profiles"""
    query = request.GET.get('search', '')
    if query:
        results = AccountUser.objects.filter(user__username__icontains=query)
    else:
        results = AccountUser.objects.none()
    context = {
        'query': query,
        'results': results, 
    }
    return render(request, 'social_media/search.html', context)
