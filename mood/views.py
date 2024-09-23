from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MoodTrackingForm, MoodForm
from .models import Mood


@login_required
def mood(request):
    return render(request, 'mood/mood.html')

# Mood tracking views
@login_required
def mood_tracking(request):
    if request.method == 'POST':
        form = MoodTrackingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mood_tracking')
    else:
        form = MoodTrackingForm()

    moods = Mood.objects.filter(user=request.user).order_by('-date')
    mood_data = []
    for mood in moods:
        mood_data.append([mood.date, mood.mood])

    return render(request, 'mood_tracking.html', {'moods': moods, 'form': form, 'mood_data': mood_data})


@login_required
def mood_history(request):
    moods = Mood.objects.filter(user=request.user).order_by('-date').values()
    return render(request, 'mood_history.html', {'moods': list(moods)})


@login_required
def log_mood(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            mood = form.save(commit=False)
            mood.user = request.user
            mood.save()
            return redirect('set_goals')
    else:
        form = MoodForm()
    return render(request, 'mood/log_mood.html', {'form': form})
def homepage(request):
    return render(request, 'homepage.html')