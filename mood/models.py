# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)