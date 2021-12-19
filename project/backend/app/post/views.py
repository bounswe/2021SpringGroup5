from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests.api import post

from register.models import Follow
from .models import Application, EquipmentComment, EventComment
from post.models import Badge, SkillLevel, Sport, EquipmentPost,EventPost,BadgeOfferedByEventPost,EquipmentPostActivtyStream, Application
from django.utils.dateparse import parse_datetime
from post.serializers import BadgeOfferedByEventPostSerializer, BadgeSerializer, EquipmentPostActivityStreamSerializer, \
    EquipmentPostSerializer, EventPostActivityStreamSerializer, EventPostSerializer, SkillLevelSerializer, SportSerializer, ApplicationSerializer
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
from django.core import serializers
# Create your views here.

from django.apps import apps
User = apps.get_model('register', 'User')
InterestLevel = apps.get_model('register', 'InterestLevel')

def process_string(s):
    if s != None and (type(s)==str):
        return unidecode(s.lower())
    return s

@login_required()
@api_view(['GET','POST'])
def createEventPost(request):
    if request.method=='POST':
        
        data=json.loads(request.POST.get('json'))
        

        post_name=data["object"]["post_name"]
        sport_category=data["object"]["sport_category"]
        longitude=data["object"]["longitude"]
        latitude=data["object"]["latitude"]
        description=data["object"]["description"]
        #image=data["object"]["pathToEventImage"]
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

        actor_id=data["actor"]["Id"]
        sport_category=process_string(sport_category)

        if spectator_limit==None:
            spectator_limit=0
        try:
            actor=list(User.objects.filter(Id=actor_id).values('Id','name','username','surname'))[0]
        except:
            return Response({"message":"There is no such user in the system"},404)

        event_status="upcoming"
        capacity="open to applications"
        #Check if the date_time is valid
        try:
            date_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        except:
            res={"message":"Invalid event time"}
            return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY) 
        
        # There is already a sport with this name in the database
        try:
            sport=Sport.objects.get(sport_name=sport_category)
            sport_id=sport.id
            sport_name=sport.sport_name
        except:
            sport_ser=SportSerializer(data={"sport_name":sport_category,"is_custom":True})
            if sport_ser.is_valid():
                sport_ser.save()
                sport_id=sport_ser.data["id"]
                sport_name=sport_ser.data["sport_name"]
            #Sport name has too many caharacters
            else:
                res={"message":"Sport name is too long"}
                return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY)

       
        skill_requirement=SkillLevel.objects.get(level_name=skill_requirement_info)
        created_date=datetime.datetime.now()

        for i in range(repeating_frequency):
            if i!=0:
                week=datetime.timedelta(weeks=i)
                current_event_date=(date_time+week).strftime("%Y-%m-%d %H:%M:%S")
            else:
                current_event_date=date_time.strftime("%Y-%m-%d %H:%M:%S")
            
            image=""

            event={"post_name":post_name,"owner":actor_id,"sport_category":sport_id,\
                "created_date":created_date+datetime.timedelta(hours=3),"description":description,\
                "longitude":longitude,"latitude":latitude,"date_time":current_event_date,"participant_limit":participant_limit,"spectator_limit":spectator_limit,\
                    "rule":rule,"equipment_requirement":equipment_requirement, "status":event_status,"capacity":capacity,\
                        "location_requirement":location_requirement,"contact_info":contact_info,\
                            "pathToEventImage":image,"skill_requirement":skill_requirement.id}

            event_ser=EventPostSerializer(data=event)
            if event_ser.is_valid():
                event_ser.save()
                try:
                    img=request.FILES["image"]
                    url="https://nzftk20rg4.execute-api.eu-central-1.amazonaws.com/v1/lodobucket451?file="
                    extension="EventPost_"+str(event_ser.data["id"])+".jpg"
                    r = requests.post(url+extension, data = img)
                    image=url+extension
                    EventPost.objects.filter(id=event_ser.data["id"]).update(pathToEventImage=image)

                except:
                    pass

                event_act_stream_ser=EventPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
                "type":data["type"],"actor":data["actor"]["Id"],"object":event_ser.data["id"]})
                if event_act_stream_ser.is_valid():
                    event_act_stream_ser.save()
                else:
                    continue
                for badge_info in badges:
                    badge_id=badge_info["id"]
                    badge_event_ser=BadgeOfferedByEventPostSerializer(data={"post":event_ser.data["id"],"badge":badge_id})
                    if badge_event_ser.is_valid():
                        badge_event_ser.save()
                        
                
            
            else:
                return Response({"message":event_ser.errors},406)

        del data["actor"]["type"]
        del data["object"]["type"]
        
        data["actor"]["type"]="Person"
        res=event_ser.data
        res["pathToEventImage"]=image
        res["owner"]=actor
        res["type"]="EventPost"
        res["created_date"]= created_date.strftime("%Y-%m-%d %H:%M:%S")
        res["date_time"]=str(date_time)
        res["skill_requirement"]=skill_requirement.level_name
        res["sport_category"]=sport_name
        res["type"]="EventPost"
        res["badges"]=badges
        data["object"]=res
        return Response(data,status=status.HTTP_201_CREATED)

    # It is a get request, badges in the db should be returned
    else:
        badges=list(Badge.objects.values())
        sports=list(Sport.objects.filter(is_custom=False).values('id',"sport_name"))
        skill_levels=list(SkillLevel.objects.values())
        res={"badges":badges,"sports":sports,"skill_levels":skill_levels}
        return Response(res,status=status.HTTP_200_OK)

@login_required()
@api_view(['GET','POST'])
def createEquipmentPost(request):
    if request.method=='POST':
        #data=request.data
        data=json.loads(request.POST.get('json'))
        owner_id=data["object"]["owner_id"]
        equipment_post_name=data["object"]["post_name"]
        sport_category=data["object"]["sport_category"]
        longitude=data["object"]["longitude"]
        latitude=data["object"]["latitude"]
        description=data["object"]["description"]
        #image=data["object"]["pathToEquipmentPostImage"]
        link=data["object"]["link"]

        try:
            actor=list(User.objects.filter(Id=owner_id).values('Id','name','surname','username'))[0]
        except:
            return Response({"message":"There is no such user in the system"},404)

        sport_category=process_string(sport_category)
        
        try:
            sport=Sport.objects.get(sport_name=sport_category)
            sport_id=sport.id
            sport_name=sport.sport_name
        except:
            sport_ser=SportSerializer(data={"sport_name":sport_category,"is_custom":True})
            if sport_ser.is_valid():
                sport_ser.save()
                sport_id=sport_ser.data["id"]
                sport_name=sport_ser.data["sport_name"]
            #Sport name has too many caharacters
            else:
                res={"message":"Sport name is too long"}
                return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        active=True
        created_date=datetime.datetime.now()
        image=""
        equipment_post_ser=EquipmentPostSerializer(data={"post_name":equipment_post_name,"owner":owner_id,"sport_category":sport_id,"created_date":created_date+datetime.timedelta(hours=3),\
            "description":description,"longitude":longitude,"latitude":latitude,"link":link,"active":active,"pathToEquipmentPostImage":image})

        if equipment_post_ser.is_valid():
            equipment_post_ser.save()
            try:
                img=request.FILES["image"]
                url="https://nzftk20rg4.execute-api.eu-central-1.amazonaws.com/v1/lodobucket451?file="
                extension="EquipmentPost_"+str(equipment_post_ser.data["id"])+".jpg"
                r = requests.post(url+extension, data = img)
                image=url+extension
                EquipmentPost.objects.filter(id=equipment_post_ser.data["id"]).update(pathToEquipmentPostImage=image)
            except:
                pass
        else:
            return Response({"message":"there was an error while deleting the equipment post"},status=status.HTTP_406_NOT_ACCEPTABLE)
        
        equipment_post_act_stream_ser=EquipmentPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
            "actor":owner_id,"type":data["type"],"object":equipment_post_ser.data["id"]})

        if equipment_post_act_stream_ser.is_valid():
            equipment_post_act_stream_ser.save()
        else:
            return Response({"message":"there was an error while deleting the equipment post"},status=status.HTTP_406_NOT_ACCEPTABLE)

        res=equipment_post_ser.data
        res["pathToEquipmentPostImage"]=image
        res["owner"]=actor
        res["sport_category"]=sport_name
        res["created_date"]=created_date.strftime("%Y-%m-%d %H:%M:%S")
        res["type"]="EquipmentPost"
        result={"@context":data["@context"],"summary":data["summary"],"type":data["type"],"actor":data["actor"],"object":res}
        return Response(result,status=status.HTTP_201_CREATED)

    # GET request
    else:
        sports=list(Sport.objects.filter(is_custom=False).values("id","sport_name"))
        res={"sports":sports}
        return Response(res,status=status.HTTP_200_OK)

@login_required()
@api_view(['DELETE'])
def deleteEquipmentPost(request):
    data=request.data

    actor_id=data["actor"]["Id"]
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
@api_view(['DELETE'])
def deleteEventPost(request):
    data = request.data

    actor_id = data["actor"]["Id"]
    event_post_id = data["object"]["post_id"]

    try:
        actor = User.objects.get(Id=actor_id)
    except:
        return Response({"message": "There is no such user in the system"}, 404)



    try:
        EventPost.objects.filter(pk=event_post_id).update(status="cancelled", capacity="cancelled")
        event_post = EventPost.objects.get(id=event_post_id)
    except:
        return Response({"message": "There is no such event in the database, deletion operation is aborted"},
                        status=status.HTTP_404_NOT_FOUND)

    event_post_ser = EventPostActivityStreamSerializer(
        data={"context": data["@context"], "summary": data["summary"], \
              "actor": actor_id, "type": data["type"], "object": event_post_id})

    if event_post_ser.is_valid():
        event_post_ser.save()
    else:
        return Response({"message": "there was an error while deleting the event post"}, status=status.HTTP_406_NOT_ACCEPTABLE)

    return Response({"message": "Event post is deleted"}, status=status.HTTP_200_OK)




@login_required()
@api_view(['POST'])
def applyToEvent(request):
    data = request.data

    actor_id = data["actor"]["Id"]
    event_id = data["event_id"]


    # Try if the user is valid
    try:
        actor = User.objects.get(Id=actor_id)
    except:
        return Response({"message": "There is no such user in the system"}, 404)
    # Try if event is in the database
    try:
        event_post=EventPost.objects.get(id=event_id)
    except:
        return Response({"message":"There is no such event in the database, deletion operation is aborted"},status=status.HTTP_404_NOT_FOUND)


    if not (event_post.capacity == "open to applications" and event_post.status == "upcoming"):                     # if the event is not open to applications or event status is
        return Response({"message": "Event is closed to applications"}, status=400)         # event is full, passed or cancelled       HTTP412 maybe??


    event_post_sport_id = event_post.sport_category_id
    event_skill_requirement = event_post.skill_requirement_id  # bunu dene id olarak yaziyor ama kelime olarak nasil olduguna bak
    isAdequate = True


    try:
        users_skill_level = InterestLevel.objects.get(owner_of_interest_id=actor_id, sport_name_id=event_post_sport_id)     # eger actor bu spor id icin skill level kaydetmediyse error olup except'e dusuyor adequate false aliyor
    except:
        return Response({"message": "There was an error about getting users skill level"}, status=status.HTTP_404_NOT_FOUND)

    try:
        users_skill_level_id = SkillLevel.objects.get(level_name=str(users_skill_level.skill_level))
    except:
        return Response({"message": "There was an error about getting users skill level"}, status=status.HTTP_404_NOT_FOUND)


    if users_skill_level_id.id >= event_skill_requirement:
        isAdequate = True
    elif users_skill_level.skill_level >= event_skill_requirement:
        isAdequate = False


    applicationStatus = "waiting"
    if not isAdequate:
        applicationStatus = "inadeq"


    application_ser=ApplicationSerializer(data={"user":actor_id, "event_post":event_post.id, "status":applicationStatus, "applicant_type":"player"})

    if application_ser.is_valid():
        try:
            application_ser.save()
        except:
            return Response({"message": "There was an error about application serializer. You may have already applied."}, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response({"message": "There was an error about application serializer"}, status=status.HTTP_406_NOT_ACCEPTABLE)


    return Response({"message":"Application is successfully created"},status=status.HTTP_201_CREATED)


@login_required()
@api_view(['POST'])
def acceptApplicant(request):
    data = request.data

    applicant_id = data["applicant_Id"]
    event_id = data["event_Id"]

    # Try if the user is valid
    try:
        actor = User.objects.get(Id=applicant_id)
    except:
        return Response({"message": "There is no such user in the system"}, 404)
    # Try if event is in the database
    try:
        event_post=EventPost.objects.get(id=event_id)
    except:
        return Response({"message":"There is no such event in the database, deletion operation is aborted"},status=status.HTTP_404_NOT_FOUND)


    try:
        application = Application.objects.filter(event_post_id=event_id, user_id=applicant_id)
        event_post = EventPost.objects.get(id=event_id)
    except:
        return Response({"message": "There is no such application in the database, operation is aborted"}, status=status.HTTP_404_NOT_FOUND)


    if event_post.participant_limit > event_post.current_player and event_post.status == "upcoming" and event_post.capacity == "open to applications":
        new_part = event_post.current_player+1
        if new_part == event_post.participant_limit:
            EventPost.objects.filter(pk=event_id).update(capacity="full", current_player=new_part)
        else:
            EventPost.objects.filter(pk=event_id).update(current_player=new_part)
    else:
        return Response({"message": "The event is not available to accept the application. Full, cancelled or maybe past"}, status=status.HTTP_400_BAD_REQUEST)


    application = application.update(status="accepted")
    return Response({"message":"Application is accepted"},status=status.HTTP_200_OK)

@login_required()  
@api_view(['PATCH'])
def changeEquipmentInfo(request):
    data=request.data

    actor_id=data["actor"]["Id"]
    post_id=data["object"]["post_id"]
    try:
        actor=list(User.objects.filter(Id=actor_id).values('Id','name','surname','username'))[0]
    except:
        return Response({"message":"There is no such user in the system"},404)

    try:
        equipment_post=EquipmentPost.objects.get(id=post_id)
    except:
        return Response({"message":"There is no such post in the database"},404)

    modifications_keys=data["modifications"].keys()
   
    equipment_post_act_ser=EquipmentPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
    "actor":actor_id,"type":data["type"],"object":equipment_post.id})



    if equipment_post_act_ser.is_valid():

        if "sport_category" in modifications_keys:
            try:
                s=Sport.objects.get(sport_name=data["modifications"]["sport_category"])
                data["modifications"]["sport_category"]=s.id
            except:
                sport_ser=SportSerializer(data={"sport_name":data["modifications"]["sport_category"],"is_custom":True})
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

    equipment_post_updated["owner"]=actor
    equipment_post_updated["created_date"]=equipment_post_updated["created_date"].strftime('%Y-%m-%d %H:%M:%S')
    res={"@context":data["@context"],"summary":data["summary"],"actor":data["actor"],"type":data["type"],"object":equipment_post_updated}
    return Response(res,200)


@login_required()  
@api_view(['PATCH'])
def changeEventInfo(request):
    data=request.data
    actor_id=data["actor"]["Id"]
    post_id=data["object"]["post_id"]
    try:
        actor=list(User.objects.filter(Id=actor_id).values('Id','name','surname','username'))[0]
    except:
        return Response({"message":"There is no such user in the system"},404)

    try:
        event_post=EventPost.objects.get(id=post_id)
    except:
        return Response({"message":"There is no such post in the database"},404)

    modifications_keys=data["modifications"].keys()
   
    event_post_act_ser=EventPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
    "actor":actor_id,"type":data["type"],"object":event_post.id})

    if event_post_act_ser.is_valid():

        if "sport_category" in modifications_keys:
            try:
                s=Sport.objects.get(sport_name=data["modifications"]["sport_category"])
                data["modifications"]["sport_category"]=s.id
            except:
                sport_ser=SportSerializer(data={"sport_name":data["modifications"]["sport_category"],"is_custom":True})
                if sport_ser.is_valid():
                    s=sport_ser.save()
                    data["modifications"]["sport_category"]=s.id
                #Sport name has too many caharacters
                else:
                    res={"message":"Sport name is too long"}
                    return Response(res,status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if "skill_requirement" in modifications_keys:
            skill=SkillLevel.objects.get(level_name=data["modifications"]["skill_requirement"])
            data["modifications"]["skill_requirement"]=skill.id
       

        event_post_ser = EventPostSerializer(event_post, data=data["modifications"], partial=True)
        if event_post_ser.is_valid():
            event_post_updated=model_to_dict(event_post_ser.save())
            event_post_updated["sport_category"]=Sport.objects.get(id=event_post_updated["sport_category"]).sport_name
            event_post_updated["skill_requirement"]=SkillLevel.objects.get(id=event_post_updated["skill_requirement"]).level_name
            if "badges" in modifications_keys:
                for badge_ in data["modifications"]["badges"]:
                    badge_id=badge_["id"]
                    badge_ser=BadgeOfferedByEventPostSerializer(data={"post":post_id,"badge":badge_id})
                    if badge_ser.is_valid():
                        BadgeOfferedByEventPost.objects.filter(post=event_post).delete()
                        badge_ser.save()
                    else:
                        return Response({"message":badge_ser.errors},422)

            event_post_act_ser.save()
        else:
            return Response({"message":event_post_ser.errors},422)

    else:
        return Response({"message":"There was an error while updating the event post"},status=status.HTTP_406_NOT_ACCEPTABLE)

    event_post_updated["created_date"]=event_post_updated["created_date"].strftime('%Y-%m-%d %H:%M:%S')
    event_post_updated["date_time"]=event_post_updated["date_time"].strftime('%Y-%m-%d %H:%M:%S')
    event_post_updated["owner"]=actor
    event_post_updated["badges"]=list(BadgeOfferedByEventPost.objects.filter(post=post_id).values('badge__id','badge__name','badge__description','badge__pathToBadgeImage'))
    res={"@context":data["@context"],"summary":data["summary"],"actor":data["actor"],"type":data["type"],"object":event_post_updated}
    return Response(res,200)


@login_required()
@api_view(['GET'])
def getWaitingApplications(request):
    eventId = request.query_params["eventId"]
    applicationList = list(Application.objects.filter(status="waiting", applicant_type="player", event_post_id=eventId).values())
    if applicationList != []:
        return JsonResponse(applicationList, safe=False)
    else:
        return Response({"message": "Waiting applications are not found"},404)


@login_required()
@api_view(['GET'])
def getRejectedApplications(request):
    eventId = request.query_params["eventId"]
    applicationList = list(Application.objects.filter(status="rejected", applicant_type="player", event_post_id=eventId).values())
    if applicationList != []:
        return JsonResponse(applicationList, safe=False)
    else:
        return Response({"message": "Rejected applications are not found"},404)


@login_required()
@api_view(['GET'])
def getAcceptedApplications(request):
    eventId = request.query_params["eventId"]
    applicationList = list(Application.objects.filter(status="accepted", applicant_type="player", event_post_id=eventId).values())
    if applicationList != []:
        return JsonResponse(applicationList, safe=False)
    else:
        return Response({"message": "Accepted applications are not found"},404)


@login_required()
@api_view(['GET'])
def getInadequateApplications(request):
    eventId = request.query_params["eventId"]
    applicationList = list(Application.objects.filter(status="inadeq", applicant_type="player", event_post_id=eventId).values())
    if applicationList != []:
        return JsonResponse(applicationList, safe=False)
    else:
        return Response({"message": "Inadequate applications are not found"},404)


@login_required()
@api_view(['POST'])
def getEventPostDetails(request):
    data=request.data
    actor_id=data["actor"]["Id"]
    post_id=data["object"]["post_id"]
    is_event_creator=False
    try:
        actor=model_to_dict(User.objects.get(Id=actor_id))
    except:
        return Response({"message":"There is no such user in the system"},404)

    try:
        event_post_details=EventPost.objects.get(id=post_id)
        
    except:
        return Response({"message":"There is no such post in the database"},404)
    
    if actor_id==event_post_details.owner_id:
        is_event_creator=True
    
    badges_offered=list(BadgeOfferedByEventPost.objects.filter(post=post_id).values('badge__id','badge__name','badge__description','badge__pathToBadgeImage'))

    try:
        comments=list(EventComment.objects.filter(post=post_id).order_by('id').values('id','content','owner','created_date','owner__Id','owner__name',\
            'owner__surname','owner__username'))
        for i in range(len(comments)):
            comments[i]["created_date"]=comments[i]["created_date"].strftime('%Y-%m-%d %H:%M:%S')
    except:
        comments=[]

    try:
        sport=Sport.objects.get(id=event_post_details.sport_category_id).sport_name
    except:
        sport=event_post_details.sport_category_id

    skill_requirement=SkillLevel.objects.get(level_name=event_post_details.skill_requirement).level_name
    try:
        accepted_players=list(Application.objects.filter(event_post=post_id,status="accepted",applicant_type="player").values('user__Id',\
        'user__name','user__surname','user__username'))
    except:
        accepted_players=[]
    
    try:
        spectators=list(Application.objects.filter(event_post=post_id,status="accepted",applicant_type="spectator").values('user__Id',\
        'user__name','user__surname','user__username'))
    except:
        spectators=[]
    
    waiting_players=[]
    rejected_players=[]
    inadequate_player_applications=[]

    if actor_id==event_post_details.owner_id:
        try:
            waiting_players=list(Application.objects.filter(event_post=post_id,status="waiting",applicant_type="player").order_by('id').values('user__Id',\
        'user__name','user__surname','user__username'))
        except:
            waiting_players=[]
        try:
            rejected_players=list(Application.objects.filter(event_post=post_id,status="rejected",applicant_type="player").values('user__Id',\
        'user__name','user__surname','user__username'))
        except:
            rejected_players=[]
        try:
            inadequate_player_applications=list(Application.objects.filter(event_post=post_id,status="inadequate",applicant_type="player").values('user__Id',\
        'user__name','user__surname','user__username'))
        except:
            inadequate_player_applications=[]

    del data["actor"]["type"]
    del data["object"]["type"]

    event_ser=EventPostSerializer(event_post_details)
    act_str=EventPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
            "type":data["type"],"actor":data["actor"]["Id"],"object":event_ser.data["id"]})

    if act_str.is_valid():
        act_str.save()
    else:
        return Response({"message":"there was an error while viewing the event post"},status=status.HTTP_406_NOT_ACCEPTABLE)
  
    event_post_details=model_to_dict(event_post_details)
    event_post_details["skill_requirement"]=skill_requirement
    event_post_details["sport_category"]=sport
    event_post_details["comments"]=comments
    event_post_details["spectators"]=spectators
    event_post_details["inadequate_player_applications"]=inadequate_player_applications
    event_post_details["waiting_players"]=waiting_players
    event_post_details["accepted_players"]=accepted_players
    event_post_details["rejected_players"]=rejected_players
    event_post_details["owner"]=list(User.objects.filter(Id=event_post_details["owner"]).values('Id','name','surname','username'))[0]
    event_post_details["is_event_creator"]=is_event_creator
    event_post_details["badges"]=badges_offered
    event_post_details["date_time"]=event_post_details["date_time"].strftime('%Y-%m-%d %H:%M:%S')
    event_post_details["created_date"]=event_post_details["created_date"].strftime('%Y-%m-%d %H:%M:%S')
    data["actor"]["type"]="Person"
    event_post_details["type"]="EventPost"
    data["object"]=event_post_details

    return Response(data,201)

@login_required()
@api_view(['POST'])
def getEventPostAnalytics(request):
    data=request.data
    actor_id = data["actor"]["Id"]
    event_post_id = data["object"]["post_id"]

    try:
        actor = User.objects.get(Id=actor_id)
    except:
        return Response({"message": "There is no such user in the system"}, 404)

    eventPost=EventPost.objects.filter(id=event_post_id)
    owner_of_the_event=list(eventPost.values('owner__Id'))[0]["owner__Id"]
    if owner_of_the_event!=actor_id:
        return Response({"message":"You are not the creator of this event you can't see the analytics"},405)
    
    accepted_users_ids=list(Application.objects.filter(event_post=event_post_id).values('user__Id'))

    if len(accepted_users_ids)==0:
        avg=0
    else:
        total_applied_event_count=0
        for i in range(len(accepted_users_ids)):
            user_id=accepted_users_ids[i]["user__Id"]
            total_applied_event_count+=len(list(Application.objects.filter(user=user_id,status='accepted',applicant_type='player')))

        avg=total_applied_event_count/len(accepted_users_ids)

    # returning average number of events that accepted users have been accepted to other events
    data["object"]["avg_accepted_event_count_of_accepted_users"]=avg
    event_post_act_ser=EventPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
    "actor":actor_id,"type":data["type"],"object":eventPost.values('id')[0]['id']})

    if event_post_act_ser.is_valid():
        event_post_act_ser.save()
    else:
        return Response({"Your request is not executed",405})

    return Response(data,201)

@login_required()
@api_view(['POST'])
def getEquipmentPostDetails(request):
    data=request.data
    actor_id=data["actor"]["Id"]
    post_id=data["object"]["post_id"]
    is_event_creator=False
    try:
        actor=User.objects.get(Id=actor_id)
    except:
        return Response({"message":"There is no such user in the system"},404)

    try:
        equipment_post_details=EquipmentPost.objects.get(id=post_id)
    except:
        return Response({"message":"There is no such post in the database"},404)

    if actor_id==equipment_post_details.owner_id:
        is_event_creator=True

    try:
        sport=Sport.objects.get(id=equipment_post_details.sport_category_id).sport_name
    except:
        sport=equipment_post_details.sport_category_id

    try:
        comments=list(EventComment.objects.filter(post=post_id).order_by('id').values('id','content','owner','created_date','owner__Id','owner__name',\
            'owner__surname','owner__username'))
        for i in range(len(comments)):
            comments[i]["created_date"]=str(comments[i]["created_date"])
    except:
        comments=[]

    equipment_post_ser=EquipmentPostSerializer(equipment_post_details)
    act_str=EquipmentPostActivityStreamSerializer(data={"context":data["@context"],"summary":data["summary"],\
            "actor":data["actor"]["Id"],"type":data["type"],"object":equipment_post_ser.data["id"]})
    if act_str.is_valid():
        act_str.save()
    else:
        return Response({"message":"there was an error while viewing the equipment post"},status=status.HTTP_406_NOT_ACCEPTABLE)

    equipment_post_details=model_to_dict(equipment_post_details)
    equipment_post_details["sport_category"]=sport
    equipment_post_details["created_date"]=equipment_post_details["created_date"].strftime('%Y-%m-%d %H:%M:%S')
    equipment_post_details["is_event_creator"]=is_event_creator
    equipment_post_details["comments"]=comments
    equipment_post_details["type"]="EventPost"
    equipment_post_details["owner"]=list(User.objects.filter(Id=equipment_post_details["owner"]).values('Id','name','surname','username'))[0]
    res={"@context":data["@context"],"summary":data["summary"],"type":data["type"],"actor":data["actor"],"object":equipment_post_details}
    return Response(res,201)


@login_required()
@api_view(['POST'])
def spectateToEvent(request):
    data = request.data

    actor_id = data["actor"]["Id"]
    event_id = data["event_id"]

    # Try if the user is valid
    try:
        actor = User.objects.get(Id=actor_id)
    except:
        return Response({"message": "There is no such user in the system"}, 404)
    # Try if event is in the database
    try:
        event_post = EventPost.objects.get(id=event_id)
    except:
        return Response({"message": "There is no such event in the database, spectate operation is aborted"},
                        status=status.HTTP_404_NOT_FOUND)


    if  event_post.current_spectator >= event_post.spectator_limit:
        return Response({"message": "Spectator limit is full"}, status=400)

    if event_post.status != "upcoming":
        return Response({"message": "This is not an upcoming event. Maybe it is cancelled or passed."}, status=400)



    ## Increase spectator by 1
    cur_spec = event_post.current_spectator
    EventPost.objects.filter(id=event_id).update(current_spectator = cur_spec+1)


    applicationStatus = "accepted"
    application_ser = ApplicationSerializer(
        data={"user": actor_id, "event_post": event_post.id, "status": applicationStatus, "applicant_type": "spectator"})


    if application_ser.is_valid():
        try:
            application_ser.save()
        except:
            return Response(
                {"message": "There was an error about application serializer. You may have already applied."},
                status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response({"message": "There was an error about application serializer"},
                        status=status.HTTP_406_NOT_ACCEPTABLE)

    return Response({"message": "Spectate application is successfully created"}, status=status.HTTP_201_CREATED)



@login_required()
@api_view(['GET'])
def getSpectators(request):
    eventId = request.query_params["eventId"]
    applicationList = list(Application.objects.filter(applicant_type="spectator", event_post_id=eventId).values())
    if applicationList != []:
        return JsonResponse(applicationList, safe=False)
    else:
        return Response({"message": "Spectators are not found"},404)

@login_required
@api_view(['POST'])
def homePageEvents(request):
    data=request.data
    actor_id=data["actor"]["Id"]

    try:
        actor=model_to_dict(User.objects.get(Id=actor_id))
    except:
        return Response({"message":"There is no such user in the system"},404)

    following_user_ids=list(Follow.objects.filter(follower=actor_id).values('following__Id'))

    if len(following_user_ids)==0:
        return Response({"message":"No record found"},404)

    result_events=[]
    for i in range(len(following_user_ids)):
        try:
            event=model_to_dict(EventPost.objects.filter(owner=following_user_ids[i]["following__Id"],status='upcoming').last())
            sport_name=Sport.objects.get(id=event["sport_category"]).sport_name
            event["sport_category"]=sport_name
            event["skill_requirement"]=SkillLevel.objects.get(level_name=event["skill_requirement"]).level_name
            result_events.append(event)
        except:
            continue

    
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
            'sport_name': process_string(x['attributes']['name']),
            "is_custom":False
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
        badges=[{"name":"enthusiastic","description":"the trait of being overly enthusiastic","pathToBadgeImage":"https://image.shutterstock.com/image-photo/happy-enthusiastic-bearded-dad-stylish-260nw-721916131.jpg","wikiId":"Q107261265"},\
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
