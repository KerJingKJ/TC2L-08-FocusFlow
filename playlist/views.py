from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Playlist
# Create your views here.

#def playlist(response):
 #   return render(response, 'playlist/playlist.html')

def select_playlist(request):
    playlists = Playlist.objects.all()
    selected_playlist = None

    if 'playlist_id' in request.GET:
        selected_playlist = get_object_or_404(Playlist, id=request.GET['playlist_id'])

    return render(request, 'playlist/playlist.html', 
    {
        'playlists':playlists,
        'selected_playlist':selected_playlist,
    })
