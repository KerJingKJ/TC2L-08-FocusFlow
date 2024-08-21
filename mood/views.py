# moods/views.py  
from django.shortcuts import render
from django.http import HttpResponse

def mood_view(response):  
    return render(response, 'mood/mood.html')
