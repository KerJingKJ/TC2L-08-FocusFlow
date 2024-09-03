# accountss/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm

from django.urls import reverse
from django.http import HttpResponseRedirect

#def login_view(request):
    #if request.method == 'POST':
        #form = LoginForm(request.POST)
        #if form.is_valid():
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password']
            #user = authenticate(request, username=username, password=password)
            #if user is not None:
                #if user.is_active:
                    #login(request, user)
                    #request.session.modified = True  # Add this line######################
                    #print("User logged in successfully!")
                    #return redirect('homepage')
                #else:
                    #messages.error(request, 'Your account is not active.')
            #else:
                #messages.error(request, 'Invalid username or password.')
        #return render(request, 'accountss/login.html', {'form': form})
    #else:
        #form = LoginForm()
        #return render(request, 'accountss/login.html', {'form': form})
    

#def login_view(request):
    #if request.method == 'POST':
        #form = LoginForm(request.POST)
        #if form.is_valid():
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password']
            #user = authenticate(request, username=username, password=password)
            
            #if user is not None:  # Check if user exists
                #login(request, user)  # Log in the user without checking activation status
                #request.session.modified = True  # To ensure session is updated
                #print("User logged in successfully!")
                #return redirect('homepage')  # Redirect to homepage
            #else:
                #messages.error(request, 'Invalid username or password.')  # Invalid login
        #else:
            #messages.error(request, 'Please correct the errors below.')
        #return render(request, 'accountss/login.html', {'form': form})
    #else:
        #form = LoginForm()
        #return render(request, 'accountss/login.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:  # Check if user exists
                login(request, user)  # Log in the user without checking activation status
                request.session.modified = True  # Ensure session is updated
                print("User logged in successfully!")
                return redirect('homepage')  # Redirect to homepage URL
            else:
                messages.error(request, 'Invalid username or password.')  # Handle invalid login
        else:
            messages.error(request, 'Please correct the errors below.')  # Handle form validation errors
        return render(request, 'accountss/login.html', {'form': form})
    
    # If the request is GET, show the empty login form
    else:
        form = LoginForm()
        return render(request, 'accountss/login.html', {'form': form})

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
from django.shortcuts import render, redirect
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

