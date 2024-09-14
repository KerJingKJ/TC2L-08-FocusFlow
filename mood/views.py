from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MoodTrackingForm, MoodForm
from .models import Mood
from datetime import datetime


@login_required
def mood(request):
    return render(request, 'mood/mood.html')
# @login_required
# def mood_tracking(request):
#     if request.method == 'POST':
#         form = MoodTrackingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('mood_tracking')
#     else:
#         form = MoodTrackingForm()
#     return render(request, 'mood_tracking.html', {'form': form})

# @login_required
# def mood_tracking_view(request):
#     if request.method == 'POST':
#         form = MoodTrackingForm(request.POST)
#         if form.is_valid():
#             # Save the form data to the database
#             form.save()
#             return render(request, 'mood_history.html', {'message': 'Mood tracking data saved successfully'})
#     else:
#         form = MoodTrackingForm()

#     moods = Mood.objects.filter(user=request.user).order_by('-date')
#     return render(request, 'mood_tracking.html', {'moods': moods, 'form': form})


# @login_required
# def mood_history(request):
#     moods = Mood.objects.filter(user=request.user).order_by('-date')
#     return render(request, 'moods/mood_history.html', {'moods': moods})

# @login_required
# def log_mood(request):
#     if request.method == 'POST':
#         form = MoodForm(request.POST)
#         if form.is_valid():
#             mood = form.save(commit=False)
#             mood.user = request.user
#             mood.save()
#             return redirect('mood_history')
#     else:
#         form = MoodForm()
#     return render(request, 'mood/log_mood.html', {'form': form})

# def mood_list(request):
#     moods = Mood.objects.all()
#     return render(request, 'mood.html', {'moods': moods})

# Mood tracking views
# @login_required
# def mood_tracking_view(request):
#     if request.method == 'POST':
#         form = MoodTrackingForm(request.POST)
#         if form.is_valid():
#             # Save the form data to the database
#             form.save()
#             return render(request, 'mood_history.html', {'message': 'Mood tracking data saved successfully'})
#     else:
#         form = MoodTrackingForm()

#     moods = Mood.objects.filter(user=request.user).order_by('-date')
#     return render(request, 'mood_tracking.html', {'moods': moods, 'form': form})

# @login_required
# def mood_history(request):
#     moods = Mood.objects.filter(user=request.user).order_by('-date')
#     return render(request, 'mood/mood_history.html', {'moods': moods})



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
    return render(request, 'mood_tracking.html', {'moods': moods, 'form': form})

@login_required
def mood_history(request):
    moods = Mood.objects.filter(user=request.user).order_by('-date')
    return render(request, 'mood_history.html', {'moods': moods})

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
    return render(request, 'mood/log_mood.html', {'form': form})

