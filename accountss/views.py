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
            #error_message = 'Invalid username or password'
            #forgot_password_link = '<a href="{% url \'password_reset\' %}">Forgot Password?</a>'
            #return render(request, 'accountss/login.html', {'error': error_message, 'forgot_password_link': forgot_password_link})
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
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return render(request, 'create_profile.html', {'error': 'Profile not found'})
        form = ProfileForm(instance=profile)
        return render(request, 'create_profile.html', {'form': form, 'request': request})

    def post(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            return render(request, 'error.html', {'error': 'Profile not found'})
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(request, 'create_profile.html', {'form': form, 'request': request})

@login_required
def update_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return render(request, 'error.html', {'error': 'Profile not found'})

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
        else:
            return render(request, 'update_profile.html', {'u_form': u_form, 'p_form': p_form, 'error': 'Invalid form data', 'request': request})
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)
        return render(request, 'update_profile.html', {'u_form': u_form, 'p_form': p_form, 'request': request})

    return render(request, 'update_profile.html', {'u_form': u_form, 'p_form': p_form})

@login_required
def profile(request):
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





#