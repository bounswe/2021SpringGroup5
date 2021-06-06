from rest_framework.decorators import api_view
from .models import Location
from .serializers import LocationSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests


@api_view(['GET'])
def get_pollution(request):
    if request.method == 'GET':

        if 'lat' in request.GET and 'lon' in request.GET:
            url = "http://api.airvisual.com/v2/nearest_city?lat={}&lon={}&key={}".format(request.GET['lat'], request.GET['lon'], settings.API_KEY)
        elif 'user_id' in request.GET:
            user_id = request.GET['user_id']
            try:
                user_id = int(user_id)
            except:
                return Response("Invalid user_id: {}".format(user_id), status=status.HTTP_400_BAD_REQUEST)

            locations = Location.objects.filter(user_id=user_id)
            if not locations.exists():
                return Response("User with id {} has no location history.".format(user_id), status=status.HTTP_404_NOT_FOUND)


            url = "http://api.airvisual.com/v2/nearest_city?lat={}&lon={}&key={}".format(locations.first().latitude, locations.first().longitude, settings.API_KEY)
        else:
            return Response("Must provide coordinates or user id", status=status.HTTP_400_BAD_REQUEST)

        response = requests.request("GET", url)
        api_dict = response.json()
        aqi = api_dict['data']['current']['pollution']['aqius']
        response_dict = {'aqi': aqi}
        if 0 <= aqi <= 50:
            response_dict['name'] = "Good"
            response_dict['color'] = "#47e60e"
            response_dict['description'] = "Air quality is satisfactory, and air pollution poses little or no risk."
        elif 51 <= aqi <= 100:
            response_dict['name'] = "Moderate"
            response_dict['color'] = "#faff29"
            response_dict['description'] = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
        elif 101 <= aqi <= 150:
            response_dict['name'] = "Unhealthy for sensitive groups"
            response_dict['color'] = "#f08510"
            response_dict['description'] = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
        elif 151 <= aqi <= 200:
            response_dict['name'] = "Unhealthy"
            response_dict['color'] = "#ff0000"
            response_dict['description'] = "Some members of the general public may experience health effects; members of sensitive groups may experiencee more seious health effects."
        elif 201 <= aqi <= 300:
            response_dict['name'] = "Very Unhealthy"
            response_dict['color'] = "#8739c0"
            response_dict['description'] = "Health alert: The risk of health effects is increased for everyone."
        elif aqi >= 301:
            response_dict['name'] = "Hazardous"
            response_dict['color'] = "#83212f"
            response_dict['description'] = "Health warning of emergency conditions: everyone is more likely to be affected."
        else:
            return Response(status=status.HTTP_503_SERVICE_UNAVAILABLE)

        response_dict['polluiton_ts'] = api_dict['data']['current']['pollution']['ts']
        response_dict['city'] = api_dict['data']['city']
        response_dict['state'] = api_dict['data']['state']
        response_dict['country'] = api_dict['data']['country']
        response_dict['coordinates'] = api_dict['data']['location']['coordinates']

        return Response(response_dict)


@api_view(['GET', 'POST'])
def location_list(request):

    if request.method == 'GET':
        if 'user_id' in request.GET:
            locations = Location.objects.filter(user_id=request.GET['user_id'])
        else:
            locations = Location.objects.all()

        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)