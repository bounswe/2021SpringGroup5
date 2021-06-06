from django.db import models

class WeatherCondition(models.Model):
    country = models.CharField(max_length=15)
    town = models.CharField(max_length=15)
    x=models.FloatField(null=False)
    y=models.FloatField(null=False)
    description=models.CharField(max_length=50)
    degrees=models.FloatField(null=False)
    pressure=models.FloatField(null=False)
    humidity=models.FloatField(null=False)
    speed=models.FloatField(null=False)
    degreeOfWind=models.FloatField(null=False)