from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from weatherCondition.models import WeatherCondition
from weatherCondition.serializer import WeatherConditionSerializer
from rest_framework.response import Response
from rest_framework import status

def weather(method,searchTown=None):
    """
    returns a json response for get and post requests to the showWeather and weather_api functions
    """
    if method=='GET':
        res={}
        return Response(res,status=status.HTTP_200_OK)

    # If the request is POST
    else:
        # Data of the previous search is retrieved. If there is no previous search, then the dictionaryOLD is an empty dictionary
        try:
            dictionaryOLD=WeatherConditionSerializer(WeatherCondition.objects.order_by('-id')[0])
            oldData=dictionaryOLD.data
        except:
            dictionaryOLD={}
            oldData=False

        api_key=settings.WEATHER_KEY

        api='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(searchTown,api_key)

        # Request is sent to the api
        weathercon= requests.get(api).json()

        # If there is such a town then the data is retrieved
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
            
            ser=WeatherConditionSerializer(data=dictionaryNew)

            # Checks if the returned data fits the limit of the fields in the model
            if ser.is_valid():

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

                # New weather conditions are saved into the database
                newWeather.save()
                state=status.HTTP_201_CREATED
            else:   
                # Return values doesn't fit the limits of the model
                state=status.HTTP_400_BAD_REQUEST
                dictionaryNew={}
            
        else:
            # There is no such town
            dictionaryNew={}
            state=status.HTTP_404_NOT_FOUND

        dictionary={"new":dictionaryNew,"old":oldData}
        
        return Response(dictionary,status=state)

@api_view(['GET','POST'])
def showWeather(request):
    """
    renders the json response returned from the weather method with html
    """
    if request.method=='GET':
        res=weather(request.method).data
        return render(request,'weatherCondition/base.html',res)
    else:
        res=weather(request.method,request.POST.get("Town")).data
        return render(request,'weatherCondition/weatherConditions.html',res)

@api_view(['GET','POST'])
def weather_api(request):
    """
    returns the json response returned from the weather method
    """
    if request.method=='GET':
        res=weather(request.method)
        return res
    else:
        res=weather(request.method,request.POST.get("Town"))
        return res