from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MoodTrackingForm, MoodForm
from .models import Mood
from datetime import datetime

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

@login_required
def mood_history(request):
    moods = Mood.objects.filter(user=request.user).order_by('-date')
    return render(request, 'moods/mood_history.html', {'moods': moods})

@login_required
def log_mood(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            mood = form.save(commit=False)
            mood.user = request.user
            mood.save()
            return redirect('mood_history')
    else:
        form = MoodForm()
    return render(request, 'mood_log.html', {'form': form})

def mood(request):
    mood_history = [
        {'date': datetime(2022, 1, 1), 'mood': 'happy'},
        {'date': datetime(2022, 1, 2), 'mood': 'sad'},
        {'date': datetime(2022, 1, 3), 'mood': 'neutral'},
        {'date': datetime(2022, 1, 4), 'mood': 'dark'},
        {'date': datetime(2022, 1, 5), 'mood': 'light'},
    ]
    return render(request, 'mood.html', {'mood_history': mood_history})

def mood_list(request):
    moods = Mood.objects.all()
    return render(request, 'mood.html', {'moods': moods})
