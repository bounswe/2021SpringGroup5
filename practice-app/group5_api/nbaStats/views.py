'''
    Author: Salih Bedirhan Eker
    Date: 07.06.2021
'''

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
import requests

from .models import Player


@api_view(['GET', 'POST'])
def stats_api(request):

    if request.method == 'GET':               # get method renders base page
        return render(request, 'nbaStats/base.html')

    if request.method == 'POST':            # post method renders player page
        if not request.data['player_name']:
            return HttpResponse(status=400)
        url = 'https://www.balldontlie.io/api/v1/players?search=' + \
            request.data['player_name']

        # gets the data and convert it into json
        try:
            data = requests.get(url).json()
        except requests.ConnectionError:
            return HttpResponse(status=503)

        match = True                        # is there any player with this name
        status = 200                                    # true by default

        if len(data['data']) == 0:          # if there is no player
            match = False
            status = 404

        players = []                          # player list that will be send
        # for every player arrange their information
        for i in range(len(data['data'])):
            player = Player()
            player.first_name = data['data'][i]['first_name']
            player.last_name = data['data'][i]['last_name']
            player.position = data['data'][i]['position']
            player.team = data['data'][i]['team']['full_name']
            player.height = data['data'][i]['height_feet']
            player.weight = data['data'][i]['weight_pounds']
            players.append(player)

        # send the infomation and match flag
        return render(request, 'nbaStats/player.html', {'players': players, 'match': match}, status=status)
