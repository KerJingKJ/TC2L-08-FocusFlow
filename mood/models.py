# Create your models here.

    
# from django.db import models
# from django.contrib.auth.models import User

# class Mood(models.Model):
#     MOOD_CHOICES = (
#         ('happy', 'Happy'),
#         ('sad', 'Sad'),
#         ('neutral', 'Neutral'),
#         ('angry', 'Angry'),
#         ('surprised', 'Surprised'),
#     )

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username}'s mood on {self.date}"
    
# Create your models here.

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
 #   def str(self):
#        return f"{self.user.username}'s mood on {self.date}"
    

# models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

MOOD_CHOICES = (
    ('😊', 'Happy'),
    ('😐', 'Neutral'),
    ('😢', 'Sad'),
    ('😠', 'Angry'),
    ('😡', 'Furious'),
)

class Mood(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    mood = models.CharField(max_length=2, choices=MOOD_CHOICES)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s mood on {self.date}"

class MoodHistory(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    history_date = models.DateField(auto_now_add=True)
    history_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.mood.user.username}'s mood history on {self.history_date}"


class MoodTracking(models.Model):
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)
    tracking_date = models.DateField(auto_now_add=True)
    tracking_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.mood.user.username}'s mood tracking on {self.tracking_date}"

