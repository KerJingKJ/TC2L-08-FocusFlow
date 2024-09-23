# forms.py

from django import forms
from .models import Mood

class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ('mood', 'notes')

    def __init__(self, *args, **kwargs):
        super(MoodForm, self).__init__(*args, **kwargs)
        self.fields['mood'].widget = forms.Select()
        self.fields['mood'].empty_label = "Select your mood"
        self.fields['notes'].widget = forms.Textarea(attrs={'rows': 5, 'cols': 30})

