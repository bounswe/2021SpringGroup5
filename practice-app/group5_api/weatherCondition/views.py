from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from weatherCondition.models import WeatherCondition
from weatherCondition.serializer import WeatherConditionSerializer
from rest_framework.response import Response
from rest_framework import status

def weather(method,searchTown=None):
    
    if method=='GET':
        res={}
        return Response(res,status=status.HTTP_200_OK)
    else:
        try:
            dictionaryOLD=WeatherConditionSerializer(WeatherCondition.objects.order_by('-id')[0])
            oldData=dictionaryOLD.data
        except:
            dictionaryOLD={}
            oldData=False

        #town=request.POST.get('Town')
        town=searchTown
        api_key=settings.WEATHER_KEY

        api='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(town,api_key)

        weathercon= requests.get(api).json()
        if weathercon["cod"]==status.HTTP_200_OK:
            dictionaryNew={
                "country":weathercon["sys"]["country"], 
                "town":weathercon["name"], 
                "x":weathercon["coord"]["lat"],
                "y":weathercon["coord"]["lon"],
                "description":weathercon["weather"][0]["description"],
                "degrees":weathercon["main"]["temp"], 
                "pressure":weathercon["main"]["pressure"],
                "humidity":weathercon["main"]["humidity"],
                "speed":weathercon["wind"]["speed"], 
                "degreeOfWind":weathercon["wind"]["deg"]
                }
            
            newWeather=WeatherCondition(country=dictionaryNew["country"],
                town=dictionaryNew["town"],
                x=dictionaryNew["x"],
                y=dictionaryNew["y"],
                description=dictionaryNew["description"],
                degrees=dictionaryNew["degrees"],
                pressure=dictionaryNew["pressure"],
                humidity=dictionaryNew["humidity"],
                speed=dictionaryNew["speed"],
                degreeOfWind=dictionaryNew["degreeOfWind"])
            
            newWeather.save()
            state=status.HTTP_201_CREATED
        else:
            dictionaryNew={}
            state=status.HTTP_404_NOT_FOUND

        dictionary={"new":dictionaryNew,"old":oldData}
        
        return Response(dictionary,status=state)

@api_view(['GET','POST'])
def showWeather(request):
    
    if request.method=='GET':
        res=weather(request.method).data
        return render(request,'weatherCondition/base.html',res)
    else:
        res=weather(request.method,request.POST.get("Town")).data
        return render(request,'weatherCondition/weatherConditions.html',res)

@api_view(['GET','POST'])
def weather_api(request):
    
    if request.method=='GET':
        res=weather(request.method)
        return res
    else:
        res=weather(request.method,request.POST.get("Town"))
        print(res.status_code,res.data)
        return res