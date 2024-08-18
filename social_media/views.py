from django.shortcuts import render, redirect
from social_media.models import Post
from django.http import Http404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from accounts.models import AccountUser

def index(request):
    """Home page of site"""
    return render(request, 'social_media/index.html')

@login_required
def profile(request):
    """Show user profile"""
    profile = Post.objects.filter(owner=request.user).order_by('created_on')
    account_info = AccountUser.objects.filter(user=request.user).first()
    context = {
        'profile': profile,
        'account_info': account_info,
    }
    if profile is not None:
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
            return redirect('social_media:profile')
        
    return render(request, 'social_media/new_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    """Delete a post"""
    post = Post.objects.get(pk=post_id)
    if request.method != 'POST':
        post.delete()
    return redirect('social_media:profile')
    
@login_required
def post(request, post_id):
    """Show a post from user"""
    post = Post.objects.get(pk=post_id)
    if post.owner != request.user:
        raise Http404
    if post is not None:
        return render(request, 'social_media/post.html', {'post': post})
    else:
        raise Http404('Post does not exist')
    
# def feed(request):
#     """User feed"""
#     feed = Post.objects.order_by('created_on')
#     return render(request, 'social_media/profile.html', {'feed': feed})
