
from django.db import models
from django.contrib.auth.models import User


class UserProfile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,blank=False)
    about = models.CharField(default="",max_length=255)
    image = models.ImageField(default="default.jpg",upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
