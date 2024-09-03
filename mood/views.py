# moods/views.py  
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mood
from django.http import HttpResponse


def mood_view(response):  
    return render(response, 'mood/mood.html')


@login_required
def mood_tracking(request):
    if request.method == 'POST':
        # Create a new mood instance
        mood = Mood(user=request.user, mood=request.POST['mood'])
        mood.save()
        return redirect('mood_tracking')
    return render(request, 'mood_tracking.html')
