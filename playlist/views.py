from django.shortcuts import render, get_object_or_404
from .models import Playlist
# Create your views here.

#def playlist(response):
 #   return render(response, 'playlist/playlist.html')

def select_playlist(request):
    playlists = Playlist.objects.all()
    selected_playlist = None

    playlist_id = request.GET.get('playlist_id')
    if playlist_id and playlist_id.isdigit():
        selected_playlist = get_object_or_404(Playlist, id=playlist_id)
# make sure it will only render the partial selected html only, not the whole page again.
    if request.headers.get('HX-Request'):
        return render(request, 'playlist/playlist_selected.html', {
            'selected_playlist': selected_playlist,
        })

    return render(request, 'playlist/playlist.html', {
        'playlists': playlists,
        'selected_playlist': selected_playlist,
    })
