from django.shortcuts import render   
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
@login_required(login_url='login_user/')
@api_view(['POST'])
def createEventPost(request):
    data=request.POST
    _,name,surname,username,id=data["actor"]
    
    _,owner_id,name,created_date,sport_category,location,description,\
    image,date_time,participant_limit,spectator_limit,rule,equipment_requirement, \
    status, capacity, location_requirement, contact_info, skill_requirement,repeating_frequency,badges,applications =data["object"]
    
    #Check if the date_time is valid
    #date = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
    #date.day)   
     
    # İlgili event post verileir kullanılarak ve if ser.is_valid(): kullandıktan sonra dbye kaydet,
    # Offered badges'a da bir entry girilecek "badges": [ "inadequate_skill","good_teacher","friendly"] ve user_id kullanarak


    # .save() ledikten sonra state=status.HTTP_201_CREATED ile 
