# accountss/views.py

#from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate, login
#from django.contrib.auth import login
#from django.contrib import messages
#from .forms import SignUpForm

#def login_view(request):
    #if request.method == 'POST':
        #username = request.POST['username']
        #password = request.POST['password']
        
        # Validate the form
        #if not username or not password:
            #messages.error(request, 'Please enter both username and password.')
            #return render(request, 'accountss/login.html')
        
        #user = authenticate(request, username=username, password=password)
        #if user is not None:
            #login(request, user)
            #return redirect('dashboard')  # Redirect to the dashboard after login
        #else:
            #messages.error(request, 'Invalid username or password.')
            #return render(request, 'accountss/login.html')
    #return render(request, 'accountss/login.html')

#def signup(request):
    #if request.method == 'POST':
        #form = SignUpForm(request.POST)
        #if form.is_valid():
            #user = form.save()
            #login(request, user)
            #messages.success(request, 'Registration successful!')
            #return redirect('dashboard')  # Redirect to the dashboard after registration
        #else:
            #messages.error(request, 'Please correct the errors below.')
    #else:
        #form = SignUpForm()
    #return render(request, 'accountss/signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username is None or password is None:
            messages.error(request, 'Please enter both username and password.')
            return render(request, 'accountss/login.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Your account is not active.')
                return render(request, 'accountss/login.html')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'accountss/login.html')
    return render(request, 'accountss/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_active:
                login(request, user)
                messages.success(request, 'Registration successful!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Your account is not active.')
                return render(request, 'accountss/signup.html', {'form': form})
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'accountss/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'accountss/signup.html', {'form': form})