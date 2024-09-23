from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Mood, MoodHistory

@receiver(post_save, sender=Mood)
def update_mood_history(sender, instance, **kwargs):
    # Create a new MoodHistory instance
    mood_history, created = MoodHistory.objects.get_or_create(
        mood=instance,
        defaults={
            'date': instance.date,
            'mood': instance.mood,
            'notes': instance.notes,
        }
    )

    # Update the MoodHistory instance
    mood_history.date = instance.date
    mood_history.mood = instance.mood
    mood_history.notes = instance.notes
    mood_history.save()