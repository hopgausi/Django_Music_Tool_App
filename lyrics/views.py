from django.shortcuts import render, redirect
from django.contrib import messages
from . import mourits_api

def home(request):
    context = {'obj': "ob"}
    return render(request, 'lyrics/index.html', context)

def get_lyrics(request):
    return render(request, 'lyrics/get_lyrics.html')

def lyrics(request):
    if request.method == 'GET':
        if request.GET['artist'] != '' and request.GET['song'] != '':
            artist = request.GET.get('artist')
            artist = artist.title().strip()
            song = request.GET.get('song')
            song = song.title().strip()
            querystring = {"artist":artist,"song":song}
            response = mourits_api.requests.request("GET", mourits_api.url, headers=mourits_api.headers, params=querystring)
            json_response =response.json()
            if json_response.get('success') == False:
                message = "Couldn't find lyrics for the given song. Make sure information is correct"
                messages.error(request, message)
                return redirect(get_lyrics)
            else:
                song_lyric = json_response.get('result').get('lyrics')
                artist = json_response.get('artist')
                song = json_response.get('song')
                context={
                    'lyric':song_lyric,
                    'artist':artist,
                    'song':song, 
                }
        else:
            return redirect(get_lyrics)
    return render(request, 'lyrics/lyrics.html', context)