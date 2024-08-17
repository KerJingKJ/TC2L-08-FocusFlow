from django.shortcuts import render

# Create your views here.

def goals(response):
    return render(response, 'goals/goals.html')
