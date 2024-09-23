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
# @login_required
# def mood_tracking(request):
#     if request.method == 'POST':
#         form = MoodTrackingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('mood_tracking')
#     else:
#         form = MoodTrackingForm()

#     moods = Mood.objects.filter(user=request.user).order_by('-date')
#     return render(request, 'mood_tracking.html', {'moods': moods, 'form': form})

# Mood tracking views
from django.http import JsonResponse

# @login_required
# def mood_tracking(request):
#     if request.method == 'POST':
#         form = MoodTrackingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Return a JSON response with the newly created mood data
#             mood_data = {
#                 'date': form.instance.date,
#                 'mood': form.instance.mood
#             }
#             return JsonResponse(mood_data)
#         else:
#             # Return a JSON response with error messages
#             error_data = {
#                 'errors': form.errors
#             }
#             return JsonResponse(error_data, status=400)

#     else:
#         form = MoodTrackingForm()

#     moods = Mood.objects.filter(user=request.user).order_by('-date')
#     return render(request, 'mood_tracking.html', {'moods': moods, 'form': form})

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

# @login_required
# def mood_history(request):
#     moods = Mood.objects.filter(user=request.user).order_by('-date')
#     return render(request, 'mood_history.html', {'moods': moods})

@login_required
def mood_history(request):
    moods = Mood.objects.filter(user=request.user).order_by('-date').values()
    return render(request, 'mood_history.html', {'moods': list(moods)})

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

# 

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