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
    
from django.db import models
from django.contrib.auth.models import User

class Mood(models.Model):
    MOOD_CHOICES = (
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('neutral', 'Neutral'),
        ('angry', 'Angry'),
        ('surprised', 'Surprised'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s mood on {self.date}"
