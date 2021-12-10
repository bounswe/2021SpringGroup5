
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests.api import post
from post.models import Application, EquipmentComment, EventComment
from post.models import Badge,SkillLevel, Sport,EquipmentPost,EventPost,BadgeOfferedByEventPost,EquipmentPostActivtyStream

from post.serializers import BadgeOfferedByEventPostSerializer, BadgeSerializer, EquipmentPostActivityStreamSerializer, \
    EquipmentPostSerializer, EventPostActivityStreamSerializer, EventPostSerializer, SkillLevelSerializer, SportSerializer, ApplicationSerializer
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status,permissions
from django.contrib.auth.decorators import login_required
import datetime
from rest_framework.views import APIView
from unidecode import unidecode
from django.forms.models import model_to_dict
import math
from django.db.models import F, FloatField, ExpressionWrapper
from datetime import datetime
import json
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

from django.apps import apps
User = apps.get_model('register', 'User')
InterestLevel = apps.get_model('register', 'InterestLevel')

def process_string(s):
    if s != None and (type(s)==str):
        return unidecode(s.lower())
    return s

@login_required()
@api_view(['POST'])
def searchEvent(request):
    data = request.data

    data_search_func  = data["search_func"]["isName"]
    search_query      = process_string(data["search_func"]["search_query"])

    isDefaultQuery = True if search_query == "" else False
    isName = data_search_func

    isSortByLocation = data["sort_func"]["isSortedByLocation"]
    capacity = data["capacity"]


    ## Initiating the query
    eventList = EventPost.objects.filter(status="upcoming", capacity=capacity)

    if isDefaultQuery:
        pass
    elif isName:
        eventList = eventList.filter(post_name__contains=search_query)
    else:
        eventList = eventList.filter(sport_category__sport_name__contains=search_query)


    ## Filters

    isFilteredByDate = False if data["filter_func"]["date"] == None else True
    if isFilteredByDate:
        filter_start_date = data["filter_func"]["date"]["startDate"]
        filter_end_date   = data["filter_func"]["date"]["endDate"]
        start_date_time_obj = datetime.strptime(filter_start_date, '%d/%m/%Y:%H')
        end_date_time_obj = datetime.strptime(filter_end_date, '%d/%m/%Y:%H')

        eventList = eventList.filter(date_time__gte=start_date_time_obj, date_time__lte=end_date_time_obj)

    isFilteredByLocation = False if data["filter_func"]["location"] == None else True
    if isFilteredByLocation:
        location_lat = data["filter_func"]["location"]["lat"]
        location_lng = data["filter_func"]["location"]["lng"]
        location_radius = data["filter_func"]["location"]["radius"]

        eventList = eventList.annotate(delta=ExpressionWrapper(((F('latitude') - location_lat) ** 2) + ((F('longitude') - location_lng) ** 2), output_field = FloatField())).filter(delta__lte=location_radius**2)

    isFilteredBySport = False if data["filter_func"]["sportType"] == "" else True
    if isFilteredBySport:
        filter_sport = data["filter_func"]["sportType"]

        eventList = eventList.filter(sport_category__sport_name__contains=filter_sport)

    if isSortByLocation:
        eventList = eventList.annotate(delta=ExpressionWrapper(((F('latitude') - location_lat) ** 2) + ((F('longitude') - location_lng) ** 2), output_field = FloatField())).order_by('delta')
    else:                                   ## else the data must be sorted by date
        eventList = eventList.order_by('date_time')


    result = serializers.serialize('json', eventList)
    return HttpResponse(result, content_type="application/json")
