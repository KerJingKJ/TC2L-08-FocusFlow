# Create your models here.
  
# models.py
    
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def str(self):
        return self.user.username