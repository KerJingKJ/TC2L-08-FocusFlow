# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput())
    first_name = forms.CharField(max_length=100, help_text='Optional')
    last_name = forms.CharField(max_length=100, help_text='Optional')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        help_texts = {
            'password1': 'Enter a strong password',
            'password2': 'Confirm your password',
        }


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput())
    first_name = forms.CharField(max_length=100, help_text='Optional')
    last_name = forms.CharField(max_length=100, help_text='Optional')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'avatar')

    def clean_bio(self):
        bio = self.cleaned_data['bio']
        if len(bio) > 500:
            raise forms.ValidationError('Bio cannot exceed 500 characters')
        return bio

    def clean_location(self):
        location = self.cleaned_data['location']
        if len(location) > 100:
            raise forms.ValidationError('Location cannot exceed 100 characters')
        return location    


# class UserUpdateForm(UserChangeForm):
#     email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput())
#     first_name = forms.CharField(max_length=100, help_text='Optional')
#     last_name = forms.CharField(max_length=100, help_text='Optional')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name')
