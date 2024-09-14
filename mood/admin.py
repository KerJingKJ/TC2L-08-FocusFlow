# Register your models here.

from .models import Mood
from django.contrib import admin

class MoodAdmin(admin.ModelAdmin):
    list_display = ('date', 'mood', 'notes')

admin.site.register(Mood, MoodAdmin)