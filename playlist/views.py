from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def playlist(response):
    return render(response, 'playlist/playlist.html')
