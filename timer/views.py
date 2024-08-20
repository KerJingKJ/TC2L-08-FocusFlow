from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def countdown(response):
    return render(response,'countdown/countdown.html')