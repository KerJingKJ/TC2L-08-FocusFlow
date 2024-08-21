# forms.py  

from django import forms  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User  

class ProfileUpdateForm(forms.ModelForm):  
    class Meta:  
        model = User  # Specifies that we're working with the User model  
        fields = ('username', 'email', 'first_name', 'last_name')  # Specifies which fields to include in the form  

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'
        self.fields['password'].widget = forms.PasswordInput()