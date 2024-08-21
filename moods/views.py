# moods/views.py  
from django.shortcuts import render  

def mood_view(request):  
    return render(request, 'moods/mood.html')

