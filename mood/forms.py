# forms.py

from django import forms
from .models import Mood

class MoodTrackingForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ('mood', 'notes')


class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ('mood', 'notes')