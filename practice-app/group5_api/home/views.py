from django.shortcuts import render
from weatherCondition.views import weather
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def index(request):
    return render(request,'home/home.html',{})