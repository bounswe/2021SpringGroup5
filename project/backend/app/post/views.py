from django.contrib.auth.models import User
from django.shortcuts import render
from post.models import Badge,SkillLevel, Sport,EquipmentPost
from post.serializers import BadgeOfferedByEventPostSerializer, BadgeSerializer, EquipmentPostActivityStreamSerializer, \
    EquipmentPostSerializer, EventPostActivityStreamSerializer, EventPostSerializer, SkillLevelSerializer, SportSerializer
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status,permissions
from django.contrib.auth.decorators import login_required
import json
import datetime
from rest_framework.views import APIView
from unidecode import unidecode
from django.forms.models import model_to_dict
# Create your views here.

def process_string(s):
    if s != None:
        return unidecode(s.lower())
    return s

@login_required(login_url='login_user/')
@api_view(['GET','POST'])
def createEventPost(request):
    if request.method=='POST':
        
        data=json.loads(request.body)
        _,owner_id,name,sport_category,country,city,neighborhood,description,\
        image,date_time,participant_limit,spectator_limit,rule,equipment_requirement, \
        event_status, capacity, location_requirement, contact_info, skill_requirement_info,repeating_frequency,badges=data["object"].values()
        

        country=process_string(country)
        city=process_string(city)
        neighborhood=process_string(neighborhood)

        if spectator_limit==None:
            spectator_limit=0
        
        event_status="upcoming"
        capacity="open to applications"
        #Check if the date_time is valid
        try:
            date = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        except:
            res={"message":"Invalid event time"}
            return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY) 
        
        sport_category=process_string(sport_category)
        # There is already a sport with this name in the database
        try:
            sport_id=Sport.objects.get(sport_name=sport_category).id
        except:
            sport_ser=SportSerializer(data={"sport_name":sport_category})
            if sport_ser.is_valid():
                sport_ser.save()
                sport_id=sport_ser.data["id"]
            #Sport name has too many caharacters
            else:
                res={"message":"Sport name is too long"}
                return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY)

       
        skill_requirement=SkillLevel.objects.get(level_name=skill_requirement_info)
        event={"post_name":name,"owner":data["actor"]["id"],"sport_category":sport_id,"description":description,\
            "country":country,"city":city,"neighborhood":neighborhood,"date_time":date,"participant_limit":participant_limit,"spectator_limit":spectator_limit,\
                "rule":rule,"equipment_requirement":equipment_requirement, "status":event_status,"capacity":capacity,\
                    "location_requirement":location_requirement,"contact_info":contact_info,"repeating_frequency":repeating_frequency,\
                        "pathToEventImage":image,"skill_requirement":skill_requirement.id}

        event_ser=EventPostSerializer(data=event)
        if event_ser.is_valid():
            event_ser.save()
        
        else:
            return Response({"message":event_ser.errors},406)

        del data["actor"]["type"]
        del data["object"]["type"]
        

        event_act_stream_ser=EventPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
            "type":data["type"],"actor":data["actor"]["id"],"object":event_ser.data["id"]})
        if event_act_stream_ser.is_valid():
            event_act_stream_ser.save()
        else:
            return Response({"message":"there was an error while deleting the equipment post"},status=status.HTTP_406_NOT_ACCEPTABLE)

        for badge_info in badges:
            badge_id=badge_info["id"]
            badge_event_ser=BadgeOfferedByEventPostSerializer(data={"post":event_ser.data["id"],"badge":badge_id})
            if badge_event_ser.is_valid():
                badge_event_ser.save()
        
        
        res=event_ser.data
        return Response(res,status=status.HTTP_201_CREATED)

    # It is a get request, badges in the db should be returned
    else:
        badges=list(Badge.objects.values())
        sports=list(Sport.objects.values())
        skill_levels=list(SkillLevel.objects.values())
        res={"badges":badges,"sports":sports,"skill_levels":skill_levels}
        return Response(res,status=status.HTTP_200_OK)

@login_required(login_url='login_user/')
@api_view(['GET','POST'])
def createEquipmentPost(request):
    if request.method=='POST':
        data=json.loads(request.body)
        _,owner_id,equipment_post_name,sport_category,country,city,neighborhood,description,image,link=data["object"].values()
        try:
            actor=User.objects.get(id=owner_id)
        except:
            return Response({"message":"There is no such user in the system"},404)

        sport_category=process_string(sport_category)

        country=process_string(country)
        city=process_string(city)
        neighborhood=process_string(neighborhood)

        try:
            sport_id=Sport.objects.get(sport_name=sport_category).id
        except:
            sport_ser=SportSerializer(data={"sport_name":sport_category})
            if sport_ser.is_valid():
                sport_ser.save()
                sport_id=sport_ser.data["id"]
            #Sport name has too many caharacters
            else:
                res={"message":"Sport name is too long"}
                return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        active=True
        equipment_post_ser=EquipmentPostSerializer(data={"post_name":equipment_post_name,"owner":owner_id,"sport_category":sport_id,\
            "description":description,"country":country,"city":city,"neighborhood":neighborhood,"link":link,"active":active,"pathToEquipmentPostImage":image})

        if equipment_post_ser.is_valid():
            equipment_post_ser.save()
        else:
            return Response({"message":"there was an error while deleting the equipment post"},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        equipment_post_act_stream_ser=EquipmentPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
            "actor":owner_id,"type":data["type"],"object":equipment_post_ser.data["id"]})

        if equipment_post_act_stream_ser.is_valid():
            equipment_post_act_stream_ser.save()
        else:
            return Response({"message":"there was an error while deleting the equipment post"},status=status.HTTP_406_NOT_ACCEPTABLE)

        res=equipment_post_ser.data
        return Response(res,status=status.HTTP_201_CREATED)

    # GET request
    else:
        sports=list(Sport.objects.values())
        res={"sports":sports}
        return Response(res,status=status.HTTP_200_OK)

@login_required(login_url='login_user/')
@api_view(['DELETE'])
def deleteEquipmentPost(request):
    data=json.loads(request.body)

    _,actor_id,_,_,_=data["actor"].values()
    _,equipment_post_id=data["object"].values()

    try:
        actor=User.objects.get(id=actor_id)
    except:
        return Response({"message":"There is no such user in the system"},404)
    try:
        EquipmentPost.objects.filter(pk=equipment_post_id).update(active=False)
        equipment_post=EquipmentPost.objects.get(id=equipment_post_id)
    except:
        return Response({"message":"There is no such event in the database, deletion operation is aborted"},status=status.HTTP_404_NOT_FOUND)
    
    
    equipment_post_ser=EquipmentPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
        "actor":actor_id,"type":data["type"],"object":equipment_post_id})

    if equipment_post_ser.is_valid():
        equipment_post_ser.save()
    else:
        return Response({"message":"there was an error while deleting the equipment post"},status=status.HTTP_406_NOT_ACCEPTABLE)

    return Response({"message":"Equipment post is deleted"},status=status.HTTP_200_OK)

@login_required(login_url='login_user/')  
@api_view(['PATCH'])
def changeEquipmentInfo(request):
    data=json.loads(request.body)

    _,actor_id,_,_,_=data["actor"].values()
    _,post_id=data["object"].values()
    try:
        actor=User.objects.get(id=actor_id)
    except:
        return Response({"message":"There is no such user in the system"},404)

    try:
        equipment_post=EquipmentPost.objects.get(id=post_id)
    except:
        return Response({"message":"There is no such post in the database"},404)

    modifications_keys=data["modifications"].keys()
   
    equipment_post_ser=EquipmentPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
    "actor":actor_id,"type":data["type"],"object":equipment_post.id})

    if equipment_post_ser.is_valid():
       
        try:
            for key,value in data["modifications"].items():
                value=process_string(value)
                
                if key=="sport_category":
                    try:
                        sport_id=Sport.objects.get(sport_name=value).id
                        
                    except:
                        sport_ser=SportSerializer(data={"sport_name":value})
                        if sport_ser.is_valid():
                            sport_ser.save()
                            sport_id=sport_ser.data["id"]
                        #Sport name has too many caharacters
                        else:
                            res={"message":"Sport name is too long"}
                            return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY)
                    equipment_post.key=sport_id
                else:
                    equipment_post.key=value
            equipment_post.save(update_fields=modifications_keys)
        except:
            return Response({"message":"Invalid modifications, information of the post did not change"},422)
        equipment_post_ser.save()

    else:
        return Response({"message":"There was an error while updating the equipment post"},status=status.HTTP_406_NOT_ACCEPTABLE)


    res={"@context":data["@context"],"summary":data["summary"],"actor":data["actor"],"type":data["type"],"object":model_to_dict(equipment_post)}
    return Response(res,200)



# It is a script for only one time run. It can only be run by Superadmin to avoid possible security bug
# It will fill the database with sports which are fetched from Decathlon API, with necessary fields.
class SaveSportListScript(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        #max_number_of_players='P1873'
        #uses='P2283'

        url = 'https://sports.api.decathlon.com/sports/'
        response = requests.get(url)  # fetch all sports
        sportlist = response.json()['data']

        sportlist = [{  # filter fields of sports
            'name': process_string(x['attributes']['name'])
        } for x in sportlist]

        ids = []

        for sport in sportlist:  # save fetched sports to datavase
            serializer = SportSerializer(data=sport)
            if serializer.is_valid():
                serializer.save()
                ids.append(sport['id'])
            else:  # if there is an array while saving the database, return HTTP_400
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # if all save operations are successfull, return their ids, with HTTP_201
        return Response({'AcceptedIds': ids}, status=status.HTTP_201_CREATED)

# It is executed once at the initial boot of the application. Badges will be decided later and for now there is only one type of badge as an example
class SaveBadgesScript(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        badges=[{"name":"awesome player","description":"You are an awesome player","pathToBadgeImage":""}]
        for badge in badges:
            serializer=BadgeSerializer(data=badge)
            if badge.is_valid():
                serializer.save()
        return Response({"message":"Badges are saved into the database"},status=status.HTTP_201_CREATED)

# It is executed once at the initial boot of the application. Skill levels will be decided later and for now there is only one type of badge as an example
class SaveSkillLevelsScript(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        levels=[{"id":1,"level":"beginner"},{"id":2, "level":"average"},{"id":3, "level":"skilled"},\
            {"id":4,"level":"specialist"},{"id":4, "level":"expert"}]
        for level in levels:
            serializer=SkillLevelSerializer(data=level)
            if level.is_valid():
                serializer.save()
        return Response({"message":"Skill levels are saved into the database"},status=status.HTTP_201_CREATED)