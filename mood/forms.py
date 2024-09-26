#forms.py

from django import forms
from .models import Mood

class MoodForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ('mood', 'notes')

    def init(self, *args, **kwargs):
        super(MoodForm, self).init(*args, **kwargs)
        self.fields['mood'].widget = forms.Select()
        self.fields['mood'].empty_label = "Select your mood"
        self.fields['notes'].widget = forms.Textarea(attrs={'rows': 5, 'cols': 30})

class MoodTrackingForm(forms.ModelForm):
    class Meta:
        model = Mood
        fields = ('mood', 'notes', 'date')
    def init(self, *args, **kwargs):
        super(MoodTrackingForm, self).init(*args, **kwargs)
        self.fields['mood'].widget = forms.Select()
        self.fields['mood'].empty_label = "Select your mood"
        self.fields['notes'].widget = forms.Textarea(attrs={'rows': 5, 'cols': 30})
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})