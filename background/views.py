from django.shortcuts import render
from django.http import HttpResponse

# def timer(response):
#     return render(response,'background/background.html')

def background(response):
    return render(response,'background/background.html')
#request