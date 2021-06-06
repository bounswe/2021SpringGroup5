from django.db import models


class Location(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()


    class Meta:
        ordering = ['created']