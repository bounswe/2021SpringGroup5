from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests.api import post
from rest_framework_simplejwt.backends import TokenBackend
from .models import Application, EquipmentComment, EventComment

from .models import Badge, SkillLevel, Sport, EquipmentPost,EventPost,Application
from django.utils.dateparse import parse_datetime


from .serializers import BadgeSerializer, EquipmentPostActivityStreamSerializer, \
    EquipmentPostSerializer, EventPostActivityStreamSerializer, EventPostSerializer, SkillLevelSerializer, \
    SportSerializer, ApplicationSerializer, EventCommentSerializer, EventCommentActivityStreamSerializer, \
    EquipmentCommentSerializer, EquipmentCommentActivityStreamSerializer, BadgeOwnedByUser 


from rest_framework.decorators import api_view
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status,permissions
import json
from rest_framework.views import APIView
from unidecode import unidecode
from django.forms.models import model_to_dict
from django.core import serializers

import datetime


# Create your views here.

from django.apps import apps
User = apps.get_model('register', 'User')
InterestLevel = apps.get_model('register', 'InterestLevel')

def process_string(s):
    if s != None and (type(s)==str):
        return unidecode(s.lower())
    return s


@api_view(['GET','POST'])
def createEventPost(request):
    if request.method=='POST':
        
        data=json.loads(request.POST.get('json'))
        
        try:
            post_name=data["object"]["post_name"]
        except:
            return Response({"message":"Post name should not be empty"},400)
        
        try:
            sport_category=data["object"]["sport_category"]
        except:
            return Response({"message":"You have to choose a sport category"},400)

        try:
            longitude=data["object"]["longitude"]
            latitude=data["object"]["latitude"]
        except:
            longitude=None
            latitude=None
        try:
            description=data["object"]["description"]
        except:
            return Response({"message":"You should provide a description"},400)
        try:
            date_time=data["object"]["date_time"]
        except:
            return Response({"message":"You have to spesify an event time"},400)
        try:
            participant_limit=data["object"]["participant_limit"]
        except:
            return Response({"message":"You have to spesify a participant limit"},400)
        try:
            spectator_limit=data["object"]["spectator_limit"]
        except:
            return Response({"message":"You have to spesify"},400)
        try:
            rule=data["object"]["rule"]
        except:
            rule=None
        try:
            equipment_requirement=data["object"]["equipment_requirement"]
        except:
            equipment_requirement=None
        try:
            location_requirement=data["object"]["location_requirement"]
        except:
            location_requirement=None
        try:
            contact_info=data["object"]["contact_info"]
        except:
            contact_info=None
        try:
            skill_requirement_info=data["object"]["skill_requirement"]
        except:
            return Response({"message":"You have to give a skill requirement"},400)
        try:
            repeating_frequency=data["object"]["repeating_frequency"]+1
        except:
            repeating_frequency=1
        token = request.headers['Authorization']
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        userId = valid_data['Id']

        actor_id = userId

        user =list(User.objects.filter(Id=actor_id).values('Id','name','username','surname'))[0]

        
        sport_category=process_string(sport_category)

        if spectator_limit==None:
            spectator_limit=0

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
                "type":data["type"],"actor":actor_id,"object":event_ser.data["id"]})
                if event_act_stream_ser.is_valid():
                    event_act_stream_ser.save()
                else:
                    continue
                
                        
                
            
            else:
                return Response({"message":event_ser.errors},406)

        del data["actor"]["type"]
        del data["object"]["type"]
        
        data["actor"]["type"]="Person"
        res=event_ser.data
        res["pathToEventImage"]=image
        res["owner"]=user
        res["type"]="EventPost"
        res["created_date"]= created_date.strftime("%Y-%m-%d %H:%M:%S")
        res["date_time"]=str(date_time)
        res["skill_requirement"]=skill_requirement.level_name
        res["sport_category"]=sport_name
        res["type"]="EventPost"
        data["object"]=res
        return Response(data,status=status.HTTP_201_CREATED)

    # It is a get request, badges in the db should be returned
    else:
        
        sports=list(Sport.objects.filter(is_custom=False).values('id',"sport_name"))
        skill_levels=list(SkillLevel.objects.values())
        res={"sports":sports,"skill_levels":skill_levels}
        return Response(res,status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def createEquipmentPost(request):
    if request.method=='POST':
        #data=request.data
        data=json.loads(request.POST.get('json'))

        token = request.headers['Authorization']
        valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
        userId = valid_data['Id']
        owner_id=userId
        equipment_post_name=data["object"]["post_name"]
        try:
            sport_category=data["object"]["sport_category"]
        except:
            return Response({"message":"You have to spesify a sport category"},400)
        try:
            longitude=data["object"]["longitude"]
            latitude=data["object"]["latitude"]
        except:
            longitude=None
            latitude=None
        try:
            description=data["object"]["description"]
        except:
            return Response({"message":"You have to write a description"},400)
        try:
            link=data["object"]["link"]
        except:
            link=None

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


@api_view(['DELETE'])
def deleteEquipmentPost(request):
    data=request.data
    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']
    actor_id = userId
    equipment_post_id=data["object"]["post_id"]

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



@api_view(['DELETE'])
def deleteEventPost(request):
    data = request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    actor_id = userId
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



@api_view(['POST'])
def applyToEvent(request):
    data = request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    actor_id = userId
    event_id = data["object"]["Id"]

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
    event_skill_requirement = event_post.skill_requirement_id
    isAdequate = True

    try:
        users_skill_level = InterestLevel.objects.get(owner_of_interest_id=actor_id, sport_name_id=event_post_sport_id)
    except:
        isAdequate = False

    if isAdequate:
        if users_skill_level.skill_level_id >= event_skill_requirement:
            isAdequate = True
        else:
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

    application_act_stream_ser = EventPostActivityStreamSerializer(data={"context":data["@context"], "summary":data["summary"], "type":data["type"], "actor":actor_id, "object":data["object"]["Id"]})
    if application_act_stream_ser.is_valid():
        application_act_stream_ser.save()

    return Response({"message":"Application is successfully created"},status=status.HTTP_201_CREATED)



@api_view(['POST'])
def acceptApplicant(request):
    data = request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    actor_id = userId
    applicant_id = data["applicant"]["Id"]
    event_id = data["object"]["Id"]

    # Try if the user is valid
    try:
        actor = User.objects.get(Id=actor_id)
    except:
        return Response({"message": "There is no such user in the system"}, 404)

    # Try if the applicant is valid
    try:
        applicant = User.objects.get(Id=applicant_id)
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

    accept_act_stream_ser = EventPostActivityStreamSerializer(data={"context":data["@context"], "summary":data["summary"], "type":data["type"], "actor":applicant_id, "object":data["object"]["Id"]})
    if accept_act_stream_ser.is_valid():
        accept_act_stream_ser.save()

    return Response({"message":"Application is accepted"},status=status.HTTP_200_OK)


@api_view(['POST'])
def rejectApplicant(request):
    data = request.data

    #actor_id = request.user.Id
    applicant_id = data["applicant"]["Id"]
    event_id = data["object"]["Id"]

    # Try if the applicant is valid
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

    application = application.update(status="rejected")
    accept_act_stream_ser = EventPostActivityStreamSerializer(data={"context": data["@context"], "summary": data["summary"], "type": data["type"], "actor": applicant_id, "object": data["object"]["Id"]})
    if accept_act_stream_ser.is_valid():
        accept_act_stream_ser.save()
    return Response({"message":"Application is rejected"},status=status.HTTP_200_OK)



@api_view(['PATCH'])
def changeEquipmentInfo(request):
    data=request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    actor_id=userId
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



@api_view(['PATCH'])
def changeEventInfo(request):
    data=request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    actor_id=userId
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
            

            event_post_act_ser.save()
        else:
            return Response({"message":event_post_ser.errors},422)

    else:
        return Response({"message":"There was an error while updating the event post"},status=status.HTTP_406_NOT_ACCEPTABLE)

    event_post_updated["created_date"]=event_post_updated["created_date"].strftime('%Y-%m-%d %H:%M:%S')
    event_post_updated["date_time"]=event_post_updated["date_time"].strftime('%Y-%m-%d %H:%M:%S')
    event_post_updated["owner"]=actor
    res={"@context":data["@context"],"summary":data["summary"],"actor":data["actor"],"type":data["type"],"object":event_post_updated}
    return Response(res,200)



@api_view(['PATCH'])
def postponeEvent(request):

    data = request.data
    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    actor_id=userId


    post_id = data["object"]["post_id"]
    try:
        actor = list(User.objects.filter(Id=actor_id).values('Id', 'name', 'surname', 'username'))[0]
    except:
        return Response({"message": "There is no such user in the system"}, 404)

    try:
        event_post = EventPost.objects.get(id=post_id)
    except:
        return Response({"message": "There is no such post in the database"}, 404)

    if actor_id != event_post.owner_id:
        return Response({"message": "You are now the owner of this event"}, 400)


    sport = Sport.objects.get(id=event_post.sport_category_id)
    skill = SkillLevel.objects.get(id=event_post.skill_requirement_id)

    new_date = datetime.datetime.strptime(data["new_date"], '%d/%m/%Y:%H')
    event_date = event_post.date_time.replace(tzinfo=None)


    if new_date >= event_date:
        EventPost.objects.filter(id=event_post.id).update(date_time=new_date)
    else:
        return Response({"message": "You entered a time that before the event date"}, 400)


    event_post_act_ser = EventPostActivityStreamSerializer(
        data={"context": data["@context"], "summary": data["summary"], "actor": actor_id, "type": data["type"], "object": event_post.id})
    if event_post_act_ser.is_valid():
        event_post_act_ser.save()
    else:
        return Response({"message": event_post_act_ser.errors}, 422)

    res = list(EventPost.objects.filter(id=event_post.id).values())
    if len(res) == 0:
        return Response({"message": "There has been an error"}, 500)
    else:
        res[0]["sport_category_id"] = sport.sport_name
        res[0]["sport_name"] = res[0].pop("sport_category_id")
        res[0]["created_date"] = res[0]["created_date"].strftime('%Y-%m-%d %H:%M:%S')
        res[0]["date_time"] = res[0]["date_time"].strftime('%Y-%m-%d %H:%M:%S')
        res[0]["skill_requirement_id"] = skill.level_name
        res[0]["skill_requirement"] = res[0].pop("skill_requirement_id")

    return HttpResponse(json.dumps(res), content_type="application/json", status=200)



@api_view(['GET'])
def getWaitingApplications(request):
    eventId = request.query_params["eventId"]
    applicationList = list(Application.objects.filter(status="waiting", applicant_type="player", event_post_id=eventId).values())
    if applicationList != []:
        return JsonResponse(applicationList, safe=False)
    else:
        return Response({"message": "Waiting applications are not found"},404)



@api_view(['GET'])
def getRejectedApplications(request):
    eventId = request.query_params["eventId"]
    applicationList = list(Application.objects.filter(status="rejected", applicant_type="player", event_post_id=eventId).values())
    if applicationList != []:
        return JsonResponse(applicationList, safe=False)
    else:
        return Response({"message": "Rejected applications are not found"},404)



@api_view(['GET'])
def getAcceptedApplications(request):
    eventId = request.query_params["eventId"]
    applicationList = list(Application.objects.filter(status="accepted", applicant_type="player", event_post_id=eventId).values())
    if applicationList != []:
        return JsonResponse(applicationList, safe=False)
    else:
        return Response({"message": "Accepted applications are not found"},404)



@api_view(['GET'])
def getInadequateApplications(request):
    eventId = request.query_params["eventId"]
    applicationList = list(Application.objects.filter(status="inadeq", applicant_type="player", event_post_id=eventId).values())
    if applicationList != []:
        return JsonResponse(applicationList, safe=False)
    else:
        return Response({"message": "Inadequate applications are not found"},404)



@api_view(['POST'])
def getEventPostDetails(request):
    data=request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    actor_id=userId
    post_id=data["object"]["post_id"]
    is_event_creator=False

    try:
        event_post_details=EventPost.objects.get(id=post_id)
        
    except:
        return Response({"message":"There is no such post in the database"},404)
    
    if actor_id==event_post_details.owner_id:
        is_event_creator=True
    
    try:
        comments=list(EventComment.objects.filter(event_post_id=post_id).order_by('id').values('id','content', 'created_date', 'owner_id__username'))
        for i in range(len(comments)):
            comments[i]["created_date"]=comments[i]["created_date"].strftime('%d/%m/%Y %H:%M')
            comments[i]["username"] = comments[i].pop("owner_id__username")
    except:
        comments=[]

    try:
        sport=Sport.objects.get(id=event_post_details.sport_category_id).sport_name
    except:
        sport=event_post_details.sport_category_id

    skill_requirement=SkillLevel.objects.get(id=event_post_details.skill_requirement.id).level_name

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
            "type":data["type"],"actor":actor_id,"object":event_ser.data["id"]})

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
    event_post_details["date_time"]=event_post_details["date_time"].strftime('%Y-%m-%d %H:%M:%S')
    event_post_details["created_date"]=event_post_details["created_date"].strftime('%Y-%m-%d %H:%M:%S')
    data["actor"]["type"]="Person"
    event_post_details["type"]="EventPost"
    data["object"]=event_post_details

    return Response(data,201)


@api_view(['POST'])
def getEventPostAnalytics(request):
    data=request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    actor_id=userId
    event_post_id = data["object"]["post_id"]

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


@api_view(['POST'])
def getEquipmentPostDetails(request):
    data=request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    actor_id=userId
    post_id=data["object"]["post_id"]
    is_event_creator=False
    

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
            "actor":actor_id,"type":data["type"],"object":equipment_post_ser.data["id"]})
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



@api_view(['POST'])
def spectateToEvent(request):
    data = request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    actor_id = userId
    event_id = data["object"]["Id"]

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

    application_act_stream_ser = EventPostActivityStreamSerializer(data={"context":data["@context"], "summary":data["summary"], "type":data["type"], "actor":actor_id, "object":data["object"]["Id"]})
    if application_act_stream_ser.is_valid():
        application_act_stream_ser.save()

    return Response({"message": "Spectate application is successfully created"}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def createEventComment(request):
    data = request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    user_id = userId

    try:
        actor=User.objects.filter(Id=user_id)
    except:
        return Response({"message":"There is no such user in the system"},404)

    try:
        event_post=EventPost.objects.get(id=data["object"]["post_id"])
    except:
        return Response({"message":"There is no such post in the database"},404)

    created_date = datetime.datetime.now()

    comment_ser = EventCommentSerializer(data={"content": data["object"]["content"], "owner": user_id, "created_date": created_date+datetime.timedelta(hours=3), "event_post": event_post.id})
    if comment_ser.is_valid():
        comment_ser.save()
    else:
        return Response({"message":"There has been an error on comment creation"},400)

    event_comment_act_stream_ser = EventCommentActivityStreamSerializer(data={"context": data["@context"], "summary": data["summary"],"type": data["type"], "actor": user_id, "object": comment_ser.data["id"]})
    if event_comment_act_stream_ser.is_valid():
        event_comment_act_stream_ser.save()

    return Response({"message": "Comment created successfully"}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def createEquipmentComment(request):
    data = request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    user_id = userId

    try:
        actor=User.objects.filter(Id=user_id)
    except:
        return Response({"message":"There is no such user in the system"},404)

    try:
        equipment_post=EquipmentPost.objects.get(id=data["object"]["post_id"])
    except:
        return Response({"message":"There is no such post in the database"},404)

    created_date = datetime.datetime.now()

    comment_ser = EquipmentCommentSerializer(data={"content": data["object"]["content"], "owner": user_id, "created_date": created_date+datetime.timedelta(hours=3), "equipment_post": equipment_post.id})
    if comment_ser.is_valid():
        comment_ser.save()
    else:
        return Response({"message":"There has been an error on comment creation"},400)

    equipment_comment_act_stream_ser = EquipmentCommentActivityStreamSerializer(data={"context": data["@context"], "summary": data["summary"],"type": data["type"], "actor": user_id, "object": comment_ser.data["id"]})
    if equipment_comment_act_stream_ser.is_valid():
        equipment_comment_act_stream_ser.save()

    return Response({"message": "Comment created successfully"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getSpectators(request):
    eventId = request.query_params["eventId"]
    applicationList = list(Application.objects.filter(applicant_type="spectator", event_post_id=eventId).values())
    if applicationList != []:
        return JsonResponse(applicationList, safe=False)
    else:
        return Response({"message": "Spectators are not found"},404)

    
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
        badges=[{"name":"enthusiastic","description":"the trait of being overly enthusiastic","wikiId":"Q107261265"},\
            {"name":"friendly","description":"relationship between people who have mutual affection for each other","wikiId":"Q491"},\
                {"name":"leader","description":"someone with the authority to affect the conduct of others; who have the responsibility of leading","wikiId":"Q1251441"},\
                    {"name":"gifted","description":"intellectual ability significantly higher than average","wikiId":"Q467677"},\
                        {"name":"loser","description":"one who loses","wikiId":"Q20861252"},\
                            {"name":"competetive","description":"trait of being competitive", "wikiId":"Q107289411"}]
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


@api_view(['GET'])
def GetEventOfUser(request):
    data = request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']

    userId = userId

    eventlist = list(EventPost.objects.filter(owner=userId).values())
    return JsonResponse(eventlist, safe=False)


@api_view(['GET'])
def GetEquipmentOfUser(request):
    data = request.data

    token = request.headers['Authorization']
    valid_data = TokenBackend(algorithm='HS256').decode(token, verify=False)
    userId = valid_data['Id']
    user = User.objects.get(Id=userId)
    equipmentlist = list(EquipmentPost.objects.filter(owner=user).values())
    return JsonResponse(equipmentlist, safe=False)



@api_view(['POST'])
def sendBadge(request):

    touser = User.objects.get(Id=request.data['to_user']['Id'])


    badge = Badge.objects.get(name=request.data['badge']['name'])
    try:
        BadgeOwnedByUser.objects.get(badge=badge, owner=touser, isGivenBySystem=False)
    except:
        BadgeOwnedByUser.objects.create(badge=badge, owner=touser, isGivenBySystem=False)
        
    return JsonResponse('SUCCESS', safe=False, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def getAllBadges(request):

    allBadges = list(Badge.objects.filter().values())
    return JsonResponse(allBadges, safe=False, status=status.HTTP_200_OK)

