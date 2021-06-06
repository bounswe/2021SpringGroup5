'''
    Author: Salih Bedirhan Eker
    Date
'''

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
import requests

from .models import Player






@api_view(['GET','POST'])
def stats_api(request):

    if request.method=='GET':               # get method renders base page
        return render(request, 'base.html')

    if request.method == 'POST':            # post method renders player page
        url = 'https://www.balldontlie.io/api/v1/players?search='+request.data['player_name']
        data = requests.get(url).json()     # gets the data and convert it into json

        match = True                        # is there any player with this name
                                            # true by default


        if len(data['data']) == 0:          # if there is no player
            match = False


        players=[]                          # player list that will be send
        for i in range(len(data['data'])):  # for every player arrange their information
            player = Player()
            player.first_name = data['data'][i]['first_name']
            player.last_name = data['data'][i]['last_name']
            player.position = data['data'][i]['position']
            player.team = data['data'][i]['team']['full_name']
            player.height = data['data'][i]['height_feet']
            player.weight = data['data'][i]['weight_pounds']
            players.append(player)

        return render(request, 'player.html', {'players':players, 'match':match})   # send the infomation and match flag
