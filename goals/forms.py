from django import forms
from .models import ToDoList

class GoalForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['title', 'description', 'completed']


class CreateGoals(forms.Form):
    goals = forms.CharField(label="Goals", max_length=200)

