# accountss/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
import logging
from django.urls import reverse

from .forms import LoginForm, SignUpForm, ProfileForm
from .models import Profile

logger = logging.getLogger(__name__)

# Login and Logout Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('profile')) # Redirect to profile view
        else:
            return render(request, 'accountss/login.html', {'error': 'Invalid username or password'})
    return render(request, 'accountss/login.html')

@login_required
def logout_view(request):
    return redirect('login')

# Signup Views
def signup_view(request):
    return render(request, 'accountss/signup.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, ('Registration successful! Please login to continue.'))
                return redirect('login')  # Redirect to login page
            except Exception as e:
                messages.error(request, ('Error creating user: {}'.format(e)))
        else:
            messages.error(request, ('Please correct the errors below.'))
    else:
        form = SignUpForm()
    return render(request, 'accountss/signup.html', {'form': form})

# Profile Views
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileForm(instance=request.user.profile)
        return render(request, 'profile.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            try:
                form.save()
                return redirect('homepage')
            except Exception as e:
                logger.error(f"Error saving profile: {e}")
                return render(request, 'profile.html', {'form': form, 'error': 'Error saving profile'})
        else:
            return render(request, 'profile.html', {'form': form})

# @login_required
# def profile(request):
#     profile = request.user.profile

# @login_required
# def profile(request):
#     profile = request.user.profile
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         form = ProfileForm(instance=profile)

#     return render(request, 'profile.html', {'form': form})

@login_required
def profile(request):
    form = ProfileForm(instance=request.user.profile) 
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile) #added request.Files to allow user to upload it
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'profile.html', {'form': form})

# Profile Display View
# @login_required
# def profile_display(request):
#     profile = request.user.profile
#     return render(request, 'accountss/profile_display.html', {'profile': profile})

@login_required
def profile_display(request):
    if hasattr(request.user, 'profile'):
        profile = request.user.profile
        return render(request, 'accountss/profile_display.html', {'profile': profile})
    else:
        return redirect('profile')

# Password Change Views
@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {'form': form})

@login_required
def password_change_done(request):
     return render(request, 'password_change_done.html')

# Homepage Views
@login_required
def home_view(request):
    return render(request, 'home.html')

def homepage(request):
    return render(request, 'homepage/homepage.html')

# views.py
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')