
# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileUpdateForm
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def accounts(response):
    return render(response,'accounts/account.html')

@login_required
def accounts(request):
    return render(request, 'accounts/account.html', {'user': request.user, 'current_year': datetime.now().year})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('account')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/account.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('home')
