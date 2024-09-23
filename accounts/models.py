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
    
class FriendRequest(models.Model):
    """Friend requests"""
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Accepted'),
        (3, 'Rejected'),
    )

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="request_sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="request_receiver")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)