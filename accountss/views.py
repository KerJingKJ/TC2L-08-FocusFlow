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
from .forms import UserUpdateForm, ProfileUpdateForm
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
        form = ProfileForm(instance=request.user)
        return render(request, 'profile.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            try:
                form.save()
                return redirect('profile')
            except Exception as e:
                logger.error(f"Error saving profile: {e}")
                return render(request, 'profile.html', {'form': form, 'error': 'Error saving profile'})
        else:
            return render(request, 'profile.html', {'form': form})

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
        profile.save()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    return render(request, 'profile.html', {'u_form': u_form, 'p_form': p_form})

@login_required
def update_profile(request):
    try:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    except Profile.DoesNotExist:
        Profile.objects.create(user=request.user)
        return redirect('profile')  # Redirect to the profile page after creating the profile
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'profile.html')


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

# Profile creation view
@login_required
def profile(request):
    try:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    except Profile.DoesNotExist:
        Profile.objects.create(user=request.user)
        return redirect('profile')  # Redirect to the profile page after creating the profile
