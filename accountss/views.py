# accountss/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    return render(request, 'accountss/signup.html')

def homepage(request):
    return render(request, 'homepage/homepage.html')


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


from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    template_name = 'accountss/logout.html'  # Optional: Template after logout
    next_page = reverse_lazy('login')  # Redirect to login page after logout



# views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')

# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from django.views import View
import logging

logger = logging.getLogger(__name__)

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

