# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=100, help_text='Optional')
    last_name = forms.CharField(max_length=100, help_text='Optional')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=100, help_text='Optional')
    last_name = forms.CharField(max_length=100, help_text='Optional')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=100, help_text='Optional')
    last_name = forms.CharField(max_length=100, help_text='Optional')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')