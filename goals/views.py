from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ToDoList
from .forms import GoalForm
# Create your views here.

@login_required
def set_goals(request):
 #   goals = ToDoList.objects.all()
    goals = ToDoList.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goals = form.save(commit=False)
            goals.user = request.user 
            goals.save()
            return redirect('set_goals')
    else:
        form = GoalForm()
   #added status bar to sum up the total goals has completed / not completed
    done = 0
    notdone = 0
    total = 0
    for goal in goals:
        if goal.completed == True:
            done += 1
        else:
            notdone += 1
    total = done + notdone
        
    if done > 0:
        bar = (done/total)*100
    else:
        bar = 0
    return render(request, 'goals/goals.html', 
        {
            'goals': goals, 
            'form': form, 
            'done':done, 
            'notdone':notdone, 
            'bar':bar,
            'total':total,
        })

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

def complete(request, goal_id, action):
    goals = get_object_or_404(ToDoList, id=goal_id)
    if action == "complete":
        goals.completed = True
        goals.save()
    else:
        goals.completed = False
        goals.save()
    return redirect('set_goals')

