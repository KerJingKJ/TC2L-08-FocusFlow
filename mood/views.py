# moods/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MoodTrackingForm, MoodForm
from .models import Mood


# View for mood tracking
@login_required
def mood_tracking(request):
    if request.method == 'POST':
        form = MoodTrackingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mood_tracking')
    else:
        form = MoodTrackingForm()
    return render(request, 'mood_tracking.html', {'form': form})


# View for mood list
def mood_list(request):
    moods = Mood.objects.all()
    return render(request, 'mood/mood_list.html', {'moods': moods})


# View for mood create
@login_required
def mood_create(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            mood = form.save(commit=False)
            mood.user = request.user
            mood.save()
            return redirect('mood_list')
    else:
        form = MoodForm()
    return render(request, 'mood/mood_create.html', {'form': form})


# View for mood history
@login_required
def mood_history(request):
    moods = Mood.objects.filter(user=request.user).order_by('-date')
    return render(request, 'moods/mood_history.html', {'moods': moods})