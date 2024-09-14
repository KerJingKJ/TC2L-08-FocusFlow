from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ToDoList
from .forms import GoalForm
from motivation.models import Actor, Quote
from playlist.models import Playlist, Track
# Create your views here.

#for to do list settings
@login_required
def set_goals(request):
    goals = ToDoList.objects.filter(user=request.user) 
    actors = Actor.objects.all()
    quotes = Quote.objects.all()
    playlists = Playlist.objects.all()
    tracks = Track.objects.all()
    form = GoalForm(request.POST)
# added the view to display it on goals page too when user select a playlist
    selected_playlist = None
    playlist_id = request.GET.get('playlist_id')
    if 'playlist_id' in request.GET and playlist_id.isdigit():
        selected_playlist = get_object_or_404(Playlist, id=request.GET['playlist_id'])

    if request.headers.get('HX-Request'):
        if playlist_id:
            return render(request, 'playlist/playlist_selected.html', {
                'selected_playlist': selected_playlist,
            })

#goals page form
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goals = form.save(commit=False)
            goals.user = request.user 
            goals.save()

            form = GoalForm()
            goals = ToDoList.objects.filter(user=request.user) 
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
            return render(request, 'goals/goals_content.html', {
                'goals': goals,
                'done': done,
                'notdone': notdone,
                'bar': bar,
                'total': total,
                'form':form,
            })   
    else:
        form = GoalForm()
# added status bar to sum up the total goals has completed / not completed

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
            'actors':actors,
            'quotes':quotes,
            'playlists':playlists,
            'tracks':tracks,
            'selected_playlist': selected_playlist,
        })

def edit(request, goal_id):
    goals = get_object_or_404(ToDoList, id=goal_id)
    
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goals)
        if request.headers.get('HX-Request'):
            form = GoalForm(request.POST, instance=goals)
            if form.is_valid():
                form.save()
                goals = ToDoList.objects.filter(user=request.user) 
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
                return render(request, 'goals/goals_content.html', 
                {
                    'goals': goals, 
                    'done':done, 
                    'notdone':notdone, 
                    'bar':bar,
                    'total':total,
                    'form':form,
                })
            else:
            # If form is invalid, return the same editing form
                return render(request, 'goals/goals_content.html', {'form': form, 'editing': True})
    else:
          form = GoalForm(instance=goals)
    return render(request, 'goals/goals_content.html', {'form': form, 'editing': True})

def delete(request, goal_id):
    goals = get_object_or_404(ToDoList, id=goal_id)
    form = GoalForm()
    if request.headers.get('HX-Request'):
        goals.delete()
        goals = ToDoList.objects.filter(user=request.user) 
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
        return render(request, 'goals/goals_content.html', 
        {
            'goals': goals, 
            'done':done, 
            'notdone':notdone, 
            'bar':bar,
            'total':total,
            'form':form,
        })
    

def complete(request, goal_id, action):
    goals = get_object_or_404(ToDoList, id=goal_id)
    form = GoalForm()
    if request.headers.get('HX-Request'):
        if action == "complete":
            goals.completed = True
            goals.save()
            goals = ToDoList.objects.filter(user=request.user) 
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
            return render(request, 'goals/goals_content.html', {
                'goals': goals,
                'done': done,
                'notdone': notdone,
                'bar': bar,
                'total': total,
                'form':form,
            })   
        else:
            goals.completed = False
            goals.save()
            goals = ToDoList.objects.filter(user=request.user) 
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
            return render(request, 'goals/goals_content.html', {
                'goals': goals,
                'done': done,
                'notdone': notdone,
                'bar': bar,
                'total': total,
                'form':form,
            })   

    return render(request, 'goals/goals_content.html', 
        {
            'goals': goals, 
            'done':done, 
            'notdone':notdone, 
            'bar':bar,
            'total':total,
            'form':form,
        })

