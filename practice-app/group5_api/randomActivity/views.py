from django.shortcuts import render

# Create your views here.

# views.py
from rest_framework import viewsets

from .serializers import ActivitySerializer
from .models import Activity
import requests


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('activity')
    serializer_class = ActivitySerializer

def showActivity(request):
    response = requests.get('http://www.boredapi.com/api/activity/')
    activityDetail = response.json()
    return render(request, 'activity/home.html', {
        'activity': activityDetail ['activity'],
	'type' : activityDetail ['type'],
	'participants' : activityDetail ['participants']

    })

