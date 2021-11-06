from django.shortcuts import render   
from django.shortcuts import render
from post.models import Badge, EventPost, Sport,BadgeOfferedByEventPost, EventPostSkillRequirements
from post.serializers import SportSerializer
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework import status

import datetime

# Create your views here.
@login_required(login_url='login_user/')
@api_view(['GET','POST'])
def createEventPost(request):
    if request.method=='POST':
        data=request.POST
        _,name,surname,username,id=data["actor"]
        
        _,owner_id,name,created_date,sport_category,location,description,\
        image,date_time,participant_limit,spectator_limit,rule,equipment_requirement, \
        status, capacity, location_requirement, contact_info, skill_requirement,repeating_frequency,badges=data["object"]
        
        status="upcoming"
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
            sport_id=Sport.objects.get(sport_name=sport_category).id
        except:
            sport_ser=SportSerializer(data={"sport_name":sport_category})
            if sport_ser.is_valid():
                sport_obj=Sport(sport_name=sport_category)
                sport_obj.save()
                sport_id=sport_obj.id
            #Sport name has too many caharacters
            else:
                res={"actor":request.POST.get("actor"),"message":"Sport name is too long"}
                return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        event={"post_name":name,"owner_id":owner_id,"sport_category_id":sport_id,"description":description,\
            "location":location,"date_time":date,"participant_limit":participant_limit,"spectator_limit":spectator_limit,\
                "rule":rule,"equipment_requirement":equipment_requirement, "status":status,"capacity":capacity,\
                    "location_requirement":location_requirement,"contact_info":contact_info,"repeating_frequency":repeating_frequency}
        event_obj=EventPost(data=event)
        event_obj.save()
        event_id=event_obj.owner_id

        for badge in badges:
            badge_id=badge["id"]
            badge_event_obj=BadgeOfferedByEventPost(data={"post_id":event_id,"badge_id":badge_id})
            badge_event_obj.save()
            
        skill_id=skill_requirement["id"]
        skill_event_obj=EventPostSkillRequirements(data={"event_post_id":event_id,"level":skill_id})
        skill_event_obj.save()
        
        res={"actor":request.POST.get("actor"),"message":"Sport event is created successfully"}
        return Response(res,status=status.HTTP_201_CREATED)

    # It is a get request, badges in the db should be returned
    else:
        badges=list(Badge.objects.all())
        sports=list(Sport.objects.all())
        res={"actor":request.GET.get("actor"),"badges":badges,"sports":sports}
        return Response(res,status=status.HTTP_200_OK)
