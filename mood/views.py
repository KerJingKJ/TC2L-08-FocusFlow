# moods/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MoodTrackingForm
from .models import Mood

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

def mood_view(request):
    moods = Mood.objects.all()
    return render(request, 'mood/mood.html', {'moods': moods})