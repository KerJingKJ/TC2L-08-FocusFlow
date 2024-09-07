# accountss/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm

from django.urls import reverse
from django.http import HttpResponseRedirect

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    print("User is active")
                    login(request, user)
                    print("User logged in successfully")
                    print("Redirecting to homepage...")
                    print(reverse('homepage'))  # Add this line
                    return redirect('homepage')
                    messages.error(request, 'Your account is not active.')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    print("Returning login page...")
    return render(request, 'accountss/login.html', {'form': form})
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
                    #print("Redirecting to homepage...")  # Add this line
                    #return redirect('homepage')
                #else:
                    #messages.error(request, 'Your account is not active.')
            #else:
                #messages.error(request, 'Invalid username or password.')
    #else:
        #form = LoginForm()

    #return render(request, 'accountss/login.html', {'form': form})

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
from django.shortcuts import render, redirect
from .forms import ProfileForm

def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})
