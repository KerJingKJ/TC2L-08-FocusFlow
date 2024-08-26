from django import forms
from .models import ToDoList

class GoalForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'description', 'completed']
        error = {'title' :{'max_length':'Title too long.'}}

