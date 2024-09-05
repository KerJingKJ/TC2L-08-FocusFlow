from django.db import models

# Create your models here.
# Music Playlist model
class Playlist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Track(models.Model):
    playlist = models.ForeignKey(Playlist, related_name='tracks', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default = "Untitled")
    audio_file = models.FileField(upload_to='tracks/')

    def __str__(self):
        return self.title


# Playlist
# lofi
# relaxing
# english songs
# korean pop 
# raining sounds (meditation music)
