# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm


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

# accounts/forms.py



from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=100, help_text='Optional')
    last_name = forms.CharField(max_length=100, help_text='Optional')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class CustomUserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'profile_picture')


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, help_text='Enter your current password')
    new_password1 = forms.CharField(max_length=100, help_text='Enter your new password')
    new_password2 = forms.CharField(max_length=100, help_text='Confirm your new password')

    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'profile_picture')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    first_name = forms.CharField(max_length=100, help_text='Optional')
    last_name = forms.CharField(max_length=100, help_text='Optional')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

#from django import forms
#from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.contrib.auth.forms import PasswordChangeForm
#from django.contrib.auth import get_user_model

#class CustomUserCreationForm(UserCreationForm):
#    email = forms.EmailField(max_length=200, help_text='Required')
 #   first_name = forms.CharField(max_length=100, help_text='Optional')
 #   last_name = forms.CharField(max_length=100, help_text='Optional')

  #  class Meta:
  #      model = get_user_model()
  #      fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

#class CustomUserUpdateForm(forms.ModelForm):
   # email = forms.EmailField()

   # class Meta:
   #     model = get_user_model()
  #      fields = ['username', 'email', 'first_name', 'last_name']

#class CustomPasswordChangeForm(PasswordChangeForm):
  #  old_password = forms.CharField(max_length=100, help_text='Enter your current password')
  #  new_password1 = forms.CharField(max_length=100, help_text='Enter your new password')
  #  new_password2 = forms.CharField(max_length=100, help_text='Confirm your new password')

   # class Meta:
   #     fields = ('old_password', 'new_password1', 'new_password2')

#class CustomUserChangeForm(UserChangeForm):
  #  class Meta:
  #      model = get_user_model()
  #      fields = ['username', 'email', 'first_name', 'last_name']

#class SignUpForm(UserCreationForm):
  #  email = forms.EmailField(max_length=200, help_text='Required')
  #  first_name = forms.CharField(max_length=100, help_text='Optional')
   # last_name = forms.CharField(max_length=100, help_text='Optional')

  #  class Meta:
  #      model = get_user_model()
   #     fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')