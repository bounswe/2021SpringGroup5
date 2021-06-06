from django.db import models

# Create your models here.


class Player:           #holds information of one player
    first_name: str
    last_name:str
    position:str
    team:str
    height:str
    weight:str