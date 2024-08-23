from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ToDoList
from .forms import GoalForm
# Create your views here.

def goals(response):
    form = ToDoList()
    return render(response,'goals/goals.html')


