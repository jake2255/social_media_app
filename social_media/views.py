from django.shortcuts import render, redirect
from social_media.models import Post
from django.http import Http404
from .forms import PostForm

def index(request):
    """Home page of site"""
    return render(request, 'social_media/index.html')

def profile(request):
    """Show user profile"""
    profile = Post.objects.order_by('created_on') # .reverse() ??
    if profile is not None:
        return render(request, 'social_media/profile.html', {'profile': profile})
    else:
        raise Http404('User profile does not exist')
    
def new_post(request):
    """Create a new post"""
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('social_media:profile')
        
    return render(request, 'social_media/new_post.html', {'form': form})

def delete_post(request, post_id):
    """Delete a post"""
    post = Post.objects.get(pk=post_id)
    if request.method != 'POST':
        post.delete()
    return redirect('social_media:profile')
    #return render(request, 'social_media/delete_post.html', {'post': post})
    

def post(request, post_id):
    """Show a post from user"""
    post = Post.objects.get(pk=post_id)
    if post is not None:
        return render(request, 'social_media/post.html', {'post': post})
    else:
        raise Http404('Post does not exist')