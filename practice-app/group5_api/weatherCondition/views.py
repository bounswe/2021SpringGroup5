from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from weatherCondition.models import WeatherCondition
from weatherCondition.serializer import WeatherConditionSerializer

@api_view(['GET','POST'])
def index(request):
    if request.method=='GET':
        return render(request,'weatherCondition/base.html',{})
    else:
        try:
            dictionaryOLD=WeatherConditionSerializer(WeatherCondition.objects.order_by('-id')[0])
        except:
            dictionaryOLD={}
        try:
            oldData=dictionaryOLD.data
        except:
            oldData=False
        town=request.POST.get('Town')
        api_key=settings.WEATHER_KEY
        api='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(town,api_key)
        weathercon= requests.get(api).json()
        if weathercon["cod"]!="404":
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

            temp=WeatherConditionSerializer(data=dictionaryNew)
            if temp.is_valid():
                dictionaryNew=temp.validated_data
                newWeather.save()
            else:
                dictionaryNew={}
        else:
            dictionaryNew={}

        dictionary={"new":dictionaryNew,"old":oldData}
        
        return render(request,'weatherCondition/weatherConditions.html',dictionary)
