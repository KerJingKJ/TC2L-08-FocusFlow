# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#class Mood(models.Model):
 #   MOOD_CHOICES = (
  #      ('happy', 'Happy'),
  #      ('sad', 'Sad'),
 #       ('angry', 'Angry'),
  #      ('fearful', 'Fearful'),
 #       ('surprised', 'Surprised'),
 #       ('neutral', 'Neutral'),
 #   )
#
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
 #   mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
 #   notes = models.TextField(blank=True)
 #   date = models.DateTimeField(default=timezone.now)
#
 #   def __str__(self):
#        return f"{self.user.username}'s mood on {self.date}"
    
# models.py
from django.db import models
from django.conf import settings


MOOD_CHOICES = (
    ('happy', 'Happy'),
    ('sad', 'Sad'),
    ('neutral', 'Neutral'),
    ('angry', 'Angry'),
    ('surprised', 'Surprised'),
)


class Mood(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s mood on {self.created_at.date()}"

class Mood(models.Model):
    date = models.DateField()
    mood = models.CharField(max_length=20)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date} - {self.mood}"