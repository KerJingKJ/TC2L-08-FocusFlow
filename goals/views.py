from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def goals(response):
    return render(response,'goals/goals.html')
