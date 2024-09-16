from django.shortcuts import render, redirect, get_object_or_404
from social_media.models import Post, Comment
from django.http import Http404
from .forms import PostForm, CommentForm
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
    profile_user = get_object_or_404(User, username=username)
    profile_account = get_object_or_404(AccountUser, user=profile_user)
    posts = Post.objects.filter(owner=profile_user).order_by('created_on')
    info = get_object_or_404(AccountUser, user=profile_user)
    friends = profile_account.friends.all()
    context = {
        'profile_user': profile_user,
        'posts': posts,
        'info': info,
        'friends': friends,
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
    comments = Comment.objects.filter(post=post)
    if not comments.exists():
        comments = None

    owner_username = post.owner.username
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = None
    context = {
        'post': post,
        'username': username,
        'owner_username': owner_username,
        'comments': comments
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

@login_required  
def new_comment(request, post_id):
    """Create a new comment on post"""
    post = get_object_or_404(Post, pk=post_id)
    owner = request.user

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.owner = owner
            new_comment.save()
            return redirect('social_media:post', post_id=post.pk)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'social_media/new_comment.html', context)