from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User

class Profile(models.Model): 
    """User profile"""
    bio = models.TextField(blank=True)
    profile_pic = ResizedImageField(size=[50,50], upload_to='accounts/images/', default='accounts/images/default/default_pfp.png', blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True, symmetrical=True)

    def __str__(self):
        return self.owner.username