from django.shortcuts import render

# Create your views here.
# Profile Views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import ProfileForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


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


@login_required
def profile(request):
    return render(request, 'profile.html')