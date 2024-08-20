from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return render(response, 'homepage/base.html')

def homepage(response):
    return render(response, 'homepage/homepage.html')
