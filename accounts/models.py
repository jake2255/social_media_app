from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User

class AccountUser(models.Model): 
    """Account user info"""
    bio = models.TextField(blank=True)
    profile_pic = ResizedImageField(size=[50,50], upload_to='accounts/images/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True, symmetrical=True)

    def __str__(self):
        return self.user.username