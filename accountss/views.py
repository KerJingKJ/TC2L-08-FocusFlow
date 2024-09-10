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

from .forms import LoginForm, CustomUserCreationForm as SignUpForm

logger = logging.getLogger(__name__)

# Authentication Views
def login_view(request):
    # Handle login form submission
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('homepage'))
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
    # Handle signup form submission
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, ('Registration successful! Please login to continue.'))
                return redirect('login')
            except Exception as e:
                messages.error(request, ('Error creating user: {}'.format(e)))
        else:
            messages.error(request, ('Please correct the errors below.'))
    else:
        form = SignUpForm()
    return render(request, 'accountss/signup.html', {'form': form})

# Homepage Views
@login_required
def home_view(request):
    return render(request, 'homepage.html')

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