from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Mood, MoodTracking, MoodHistory


@receiver(post_save, sender=Mood)
def update_mood_tracking(sender, instance, **kwargs):
    # Create a new MoodTracking instance
    mood_tracking, created = MoodTracking.objects.get_or_create(
        mood=instance,
        defaults={
            'date': instance.date,
            'mood': instance.mood,
        }
    )

    # Update the MoodTracking instance
    mood_tracking.date = instance.date
    mood_tracking.mood = instance.mood
    mood_tracking.save()

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