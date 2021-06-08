from rest_framework import serializers
from weatherCondition.models import WeatherCondition

class WeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model= WeatherCondition
        fields=['id','country','town','x','y','description','degrees','pressure','humidity','speed','degreeOfWind']
