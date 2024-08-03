from django.db import models

class Post(models.Model):
    """A post the user makes to the app."""
    caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to='social_media/images/')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.image.url