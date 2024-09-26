# Create your models here.

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

MOOD_LEVELS = {
    '😊': 4,
    '😐': 3,
    '😢': 2,
    '😠': 1,
    '😡': 0,
}

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




