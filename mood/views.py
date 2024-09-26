# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import  MoodForm
# from .models import Mood


# @login_required
# def mood(request):
#     return render(request, 'mood/mood.html')

# # Mood History
# @login_required
# def mood_history(request):
#     moods = Mood.objects.filter(user=request.user).order_by('-date').values()
#     return render(request, 'mood_history.html', {'moods': list(moods)})


# @login_required
# def log_mood(request):
#     if request.method == 'POST':
#         form = MoodForm(request.POST)
#         if form.is_valid():
#             mood = form.save(commit=False)
#             mood.user = request.user
#             mood.save()
#             return redirect('set_goals')
#     else:
#         form = MoodForm()
#     return render(request, 'mood/log_mood.html', {'form': form})
# def homepage(request):
#     return render(request, 'homepage.html')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import  MoodForm
from .models import Mood, MOOD_CHOICES, MOOD_LEVELS


@login_required
def mood(request):
    return render(request, 'mood/mood.html')

# Mood History
@login_required
def mood_history(request):
    moods = Mood.objects.filter(user=request.user).order_by('-date', '-created_at')

    mood_dates = [mood.date.strftime('%Y-%m-%d') for mood in moods]  # Convert dates to a readable format
    mood_levels =  [MOOD_LEVELS[mood.mood] for mood in moods]  # Assuming 'mood_level' holds the mood value
    mood_choices = [mood.mood for mood in moods]
    return render(request, 'mood/mood_history.html', {
        'moods': moods,
        'mood_dates': mood_dates,  # List of dates
        'mood_levels': mood_levels,
        'mood_choices': mood_choices,  # List of mood levels
    })



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

