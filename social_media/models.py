from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User

class Post(models.Model):
    """A post the user makes to the app."""
    caption = models.CharField(max_length=50)
    image = ResizedImageField(size=[250,250], upload_to='social_media/images/')
    created_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.image.url
    
class Comment(models.Model):
    """A comment a user leaves on a post."""
    comment = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment