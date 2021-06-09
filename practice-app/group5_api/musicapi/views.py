import requests
from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


def musicapi(request):
    return render(request, "musicapi/home.html")


def get_music(request):
    url = "https://api.spotify.com/v1/playlists/{}/tracks".format(
        settings.PLAYLIST_ID)
    headers = settings.TOKEN
    info = requests.get(url, headers=headers).json
    context = {
        "info": info
    }
    return render(request, "musicapi/music.html", context)


class GetMusicView(APIView):
    def get(self, request):
        url = "https://api.spotify.com/v1/playlists/{}/tracks".format(
            settings.PLAYLIST_ID)
        headers = settings.TOKEN
        r = requests.get(url, headers=headers)
        info = r.content
        json_response = r.json()
        repository = json_response['items']
        list = []
        for i in repository:
            list.append(i['track']['name'])
        return Response(list)
