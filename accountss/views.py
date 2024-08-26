# accountss/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to some dashboard
    else:
        form = UserCreationForm()
    return render(request, 'accountss/signup.html', {'form': form})

def login_view(request):
    return render(request, 'accountss/login.html')

# accounts/views.py
#from django.shortcuts import render, redirect
#from django.contrib.auth import login
#from .forms import SignUpForm

#def signup(request):
    #if request.method == 'POST':
        #form = SignUpForm(request.POST)
        #if form.is_valid():
            #user = form.save()
            #login(request, user)
            #return redirect('dashboard')  # Redirect to the dashboard after registration
    #else:
        #form = SignUpForm()
    #return render(request, 'accounts/signup.html', {'form': form})

#from django.shortcuts import render, redirect
#from django.contrib.auth import login
#from django.contrib import messages
#from .forms import SignUpForm

#def signup(request):
    #if request.method == 'POST':
        #form = SignUpForm(request.POST)
        #if form.is_valid():
            #user = form.save()
            #login(request, user)
            #messages.success(request, 'Registration successful!')
            #return redirect('dashboard')  # Redirect to the dashboard after registration
    #else:
        #form = SignUpForm()
    #return render(request, 'accounts/signup.html', {'form': form})