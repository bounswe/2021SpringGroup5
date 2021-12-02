
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests.api import post
from post.models import Badge,SkillLevel, Sport,EquipmentPost,EventPost,BadgeOfferedByEventPost,EquipmentPostActivtyStream

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

from django.apps import apps
User = apps.get_model('register', 'User')

def process_string(s):
    if s != None and (type(s)==str):
        return unidecode(s.lower())
    return s

@login_required()
@api_view(['GET','POST'])
def createEventPost(request):
    if request.method=='POST':
        
        data=request.data


        post_name=data["object"]["post_name"]
        sport_category=data["object"]["sport_category"]
        country=data["object"]["country"]
        city=data["object"]["city"]
        neighborhood=data["object"]["neighborhood"]
        description=data["object"]["description"]
        image=data["object"]["pathToEventImage"]
        date_time=data["object"]["date_time"]
        participant_limit=data["object"]["participant_limit"]
        spectator_limit=data["object"]["spectator_limit"]
        rule=data["object"]["rule"]
        equipment_requirement=data["object"]["equipment_requirement"]
        location_requirement=data["object"]["location_requirement"]
        contact_info=data["object"]["contact_info"]
        skill_requirement_info=data["object"]["skill_requirement"]
        repeating_frequency=data["object"]["repeating_frequency"]
        badges=data["object"]["badges"]

        actor_id=data["actor"]["id"]
        country=process_string(country)
        city=process_string(city)
        neighborhood=process_string(neighborhood)
        sport_category=process_string(sport_category)

        if spectator_limit==None:
            spectator_limit=0
        try:
            actor=User.objects.get(Id=actor_id)
        except:
            return Response({"message":"There is no such user in the system"},404)

        event_status="upcoming"
        capacity="open to applications"
        #Check if the date_time is valid
        try:
            date = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        except:
            res={"message":"Invalid event time"}
            return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY) 
        
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

        event={"post_name":post_name,"owner":actor_id,"sport_category":sport_id,"description":description,\
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

@login_required()
@api_view(['GET','POST'])
def createEquipmentPost(request):
    if request.method=='POST':
        data=request.data

        owner_id=data["object"]["owner_id"]
        equipment_post_name=data["object"]["post_name"]
        sport_category=data["object"]["sport_category"]
        country=data["object"]["country"]
        city=data["object"]["city"]
        neighborhood=data["object"]["neighborhood"]
        description=data["object"]["description"]
        image=data["object"]["pathToEquipmentPostImage"]
        link=data["object"]["link"]
        try:
            actor=User.objects.get(Id=owner_id)
        except:
            return Response({"message":"There is no such user in the system"},404)

        sport_category=process_string(sport_category)

        country=process_string(country)
        city=process_string(city)
        neighborhood=process_string(neighborhood)
        sport_category=process_string(sport_category)
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

@login_required()
@api_view(['DELETE'])
def deleteEquipmentPost(request):
    data=request.data

    actor_id=data["actor"]["id"]
    equipment_post_id=data["object"]["post_id"]

    try:
        actor=User.objects.get(Id=actor_id)
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

@login_required()  
@api_view(['PATCH'])
def changeEquipmentInfo(request):
    data=request.data

    actor_id=data["actor"]["id"]
    post_id=data["object"]["post_id"]
    try:
        actor=User.objects.get(Id=actor_id)
    except:
        return Response({"message":"There is no such user in the system"},404)

    try:
        equipment_post=EquipmentPost.objects.get(id=post_id)
    except:
        return Response({"message":"There is no such post in the database"},404)

    modifications_keys=data["modifications"].keys()
   
    equipment_post_act_ser=EquipmentPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
    "actor":actor_id,"type":data["type"],"object":equipment_post.id})

    data["modifications"]["country"]=process_string(data["modifications"]["country"])
    data["modifications"]["city"]=process_string(data["modifications"]["city"])
    data["modifications"]["neighborhood"]=process_string(data["modifications"]["neighborhood"])
    data["modifications"]["sport_category"]=process_string(data["modifications"]["sport_category"])


    if equipment_post_act_ser.is_valid():

        if "sport_category" in modifications_keys:
            try:
                s=Sport.objects.get(sport_name=data["modifications"]["sport_category"])
                data["modifications"]["sport_category"]=s.id
            except:
                sport_ser=SportSerializer(data={"sport_name":data["modifications"]["sport_category"]})
                if sport_ser.is_valid():
                    s=sport_ser.save()
                    data["modifications"]["sport_category"]=s.id
                #Sport name has too many caharacters
                else:
                    res={"message":"Sport name is too long"}
                    return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        equipment_post_ser = EquipmentPostSerializer(equipment_post, data=data["modifications"], partial=True)
        if equipment_post_ser.is_valid():
            equipment_post_updated=model_to_dict(equipment_post_ser.save())
            equipment_post_updated["sport_category"]=Sport.objects.get(id=equipment_post_updated["sport_category"]).sport_name
            equipment_post_act_ser.save()
        else:
            return Response({"message":equipment_post_ser.errors},422)

    else:
        return Response({"message":"There was an error while updating the equipment post"},status=status.HTTP_406_NOT_ACCEPTABLE)


    res={"@context":data["@context"],"summary":data["summary"],"actor":data["actor"],"type":data["type"],"object":equipment_post_updated}
    return Response(res,200)


@login_required()  
@api_view(['PATCH'])
def changeEventInfo(request):
    data=request.data
    actor_id=data["actor"]["id"]
    post_id=data["object"]["post_id"]
    try:
        actor=User.objects.get(Id=actor_id)
    except:
        return Response({"message":"There is no such user in the system"},404)

    try:
        event_post=EventPost.objects.get(id=post_id)
    except:
        return Response({"message":"There is no such post in the database"},404)

    modifications_keys=data["modifications"].keys()
   
    event_post_act_ser=EventPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
    "actor":actor_id,"type":data["type"],"object":event_post.id})

    data["modifications"]["country"]=process_string(data["modifications"]["country"])
    data["modifications"]["city"]=process_string(data["modifications"]["city"])
    data["modifications"]["neighborhood"]=process_string(data["modifications"]["neighborhood"])
    data["modifications"]["sport_category"]=process_string(data["modifications"]["sport_category"])

    if event_post_act_ser.is_valid():

        if "sport_category" in modifications_keys:
            try:
                s=Sport.objects.get(sport_name=data["modifications"]["sport_category"])
                data["modifications"]["sport_category"]=s.id
            except:
                sport_ser=SportSerializer(data={"sport_name":data["modifications"]["sport_category"]})
                if sport_ser.is_valid():
                    s=sport_ser.save()
                    data["modifications"]["sport_category"]=s.id
                #Sport name has too many caharacters
                else:
                    res={"message":"Sport name is too long"}
                    return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        skill=SkillLevel.objects.get(level_name=data["modifications"]["skill_requirement"])
        data["modifications"]["skill_requirement"]=skill.id

        event_post_ser = EventPostSerializer(event_post, data=data["modifications"], partial=True)
        if event_post_ser.is_valid():
            event_post_updated=model_to_dict(event_post_ser.save())
            event_post_updated["sport_category"]=Sport.objects.get(id=event_post_updated["sport_category"]).sport_name
            event_post_updated["skill_requirement"]=skill.level_name
            BadgeOfferedByEventPost.objects.filter(post=event_post).delete()
            for badge_name in data["modifications"]["badges"]:
                badge=Badge.objects.get(name=badge_name)
                badge_id=badge.id
                badge_ser=BadgeOfferedByEventPostSerializer(data={"post_id":post_id,"badge_id":badge_id})
                if badge_ser.is_valid():
                    badge_ser.save()

            event_post_act_ser.save()
        else:
            return Response({"message":event_post_ser.errors},422)

    else:
        return Response({"message":"There was an error while updating the event post"},status=status.HTTP_406_NOT_ACCEPTABLE)


    res={"@context":data["@context"],"summary":data["summary"],"actor":data["actor"],"type":data["type"],"object":event_post_updated}
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
            'sport_name': process_string(x['attributes']['name'])
        } for x in sportlist]

        sports = []

        for sport in sportlist:  # save fetched sports to datavase
            serializer = SportSerializer(data=sport)
            if serializer.is_valid():
                serializer.save()
                sports.append(sport["sport_name"])
            else:  # if there is an array while saving the database, return HTTP_400
                continue

        # if all save operations are successfull, return their ids, with HTTP_201
        return Response({'AcceptedSports': sports}, status=status.HTTP_201_CREATED)


# It is executed once at the initial boot of the application. Badges will be decided later and for now there is only one type of badge as an example
class SaveBadgesScript(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        badges=[{"name":"friendly","description":"You are a friendly player","pathToBadgeImage":""},\
            {"name":"team player","description":"You are such a team player","pathToBadgeImage":""},\
                {"name":"fair player","description":"You are a fair player","pathToBadgeImage":""},\
                    {"name":"good server","description":"You are a good server","pathToBadgeImage":""},\
                        {"name":"fast runner","description":"Wow! You were very fast","pathToBadgeImage":""}]
        for badge in badges:
            serializer=BadgeSerializer(data=badge)
            if serializer.is_valid():
                serializer.save()
        return Response({"message":"Badges are saved into the database"},status=status.HTTP_201_CREATED)

# It is executed once at the initial boot of the application. Skill levels will be decided later and for now there is only one type of badge as an example
class SaveSkillLevelsScript(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        levels=[{"level_name":"beginner"},{"level_name":"average"},{"level_name":"skilled"},\
            {"level_name":"specialist"},{"level_name":"expert"}]
        for level in levels:
            serializer=SkillLevelSerializer(data=level)
            if serializer.is_valid():
                serializer.save()
        return Response({"message":"Skill levels are saved into the database"},status=status.HTTP_201_CREATED)
