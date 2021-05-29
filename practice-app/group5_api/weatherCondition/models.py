from django.db import models

class WeatherCondition(models.Model):
    country = models.CharField(max_length=30)
    town = models.CharField(max_length=30)
    x=models.FloatField()
    y=models.FloatField()
    description=models.CharField(max_length=50)
    degrees=models.FloatField()
    pressure=models.FloatField()
    humidity=models.FloatField()
    speed=models.FloatField()
    degreeOfWind=models.FloatField()