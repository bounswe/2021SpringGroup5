from django.contrib.auth.models import User
from django.shortcuts import render
from post.models import Badge, EventPost, SkillLevel, Sport,BadgeOfferedByEventPost, EventPostSkillRequirements
from post.serializers import SportSerializer
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
import json
import datetime

# Create your views here.
@login_required(login_url='login_user/')
@api_view(['GET','POST'])
def createEventPost(request):
    if request.method=='POST':
        
        data=json.loads(request.body)
        _,owner_id,name,sport_category,location,description,\
        image,date_time,participant_limit,spectator_limit,rule,equipment_requirement, \
        event_status, capacity, location_requirement, contact_info, skill_requirement_info,repeating_frequency,badges=data["object"].values()
        
        if spectator_limit=="Null":
            spectator_limit=0
        
        event_status="upcoming"
        capacity="open to applications"
        #Check if the date_time is valid
        try:
            date = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        except:
            res={"actor":request.POST.get("actor"),"message":"Invalid event time"}
            return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY) 
        
        sport_category=sport_category.lower()
        # There is already a sport with this name in the database
        try:
            sport=Sport.objects.get(sport_name=sport_category)
        except:
            sport_ser=SportSerializer(data={"sport_name":sport_category})
            if sport_ser.is_valid():
                sport_obj=Sport(sport_name=sport_category)
                sport_obj.save()
                sport=sport_obj
            #Sport name has too many caharacters
            else:
                res={"actor":request.POST.get("actor"),"message":"Sport name is too long"}
                return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY)

       

        event={"post_name":name,"owner":request.user,"sport_category":sport,"description":description,\
            "location":location,"date_time":date,"participant_limit":participant_limit,"spectator_limit":spectator_limit,\
                "rule":rule,"equipment_requirement":equipment_requirement, "status":event_status,"capacity":capacity,\
                    "location_requirement":location_requirement,"contact_info":contact_info,"repeating_frequency":repeating_frequency,\
                        "pathToEventImage":image}
       
        event_obj=EventPost(**event)
        event_obj.save()

        for badge_info in badges:
            badge_id=badge_info["id"]
            badge=Badge.objects.get(id=badge_id)
            badge_event_obj=BadgeOfferedByEventPost(**{"post":event_obj,"badge":badge})
            badge_event_obj.save()
            
        skill_requirement=SkillLevel.objects.get(id=skill_requirement_info["id"])
        skill_event_obj=EventPostSkillRequirements(**{"event_post":event_obj,"level":skill_requirement})
        skill_event_obj.save()
        
        res={"actor":request.POST.get("actor"),"message":"Sport event is created successfully"}
        return Response(res,status=status.HTTP_201_CREATED)

    # It is a get request, badges in the db should be returned
    else:
        badges=list(Badge.objects.values())
        sports=list(Sport.objects.values())
        skill_levels=list(SkillLevel.objects.values())
        res={"badges":badges,"sports":sports,"skill_levels":skill_levels}
        return Response(res,status=status.HTTP_200_OK)
