from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoList
from .forms import GoalForm
# Create your views here.

def set_goals(request):
    goals = ToDoList.objects.all()
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goals = form.save(commit=False)
            goals.user = request.user 
            goals.save()
            return redirect('set_goals')
    else:
        form = GoalForm()
    return render(request, 'goals/goals.html', {'goals': goals, 'form': form})

def edit(request, goal_id):
    goals = get_object_or_404(ToDoList, id=goal_id)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goals)
        if form.is_valid():
            form.save()
            return redirect('set_goals')
    else:
        form = GoalForm(instance=goals)
    return render(request, 'goals/goals.html', {'form': form, 'editing': True})

def delete(request, goal_id):
    goals = get_object_or_404(ToDoList, id=goal_id)
    goals.delete()
    return redirect('set_goals')

