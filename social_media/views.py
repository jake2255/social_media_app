from django.shortcuts import render
from social_media.models import Post
from django.http import Http404

def index(request):
    """Home page of site"""
    return render(request, 'page/index.html')

def user_posts(request):
    """Show all user posts (homepage)"""
    user_posts = Post.objects.order_by('created_on')
    if user_posts is not None:
        return render(request, 'posts/user_posts.html', {'user_posts': user_posts})
    else:
        raise Http404('User posts does not exist')
    
def post(request, post_id):
    """Show a post from user"""
    post = Post.objects.get(pk=post_id)
    if post is not None:
        return render(request, 'posts/post.html', {'post': post})
    else:
        raise Http404('Post does not exist')
    
