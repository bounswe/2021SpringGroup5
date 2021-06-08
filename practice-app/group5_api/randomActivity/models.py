from django.db import models

# Create your models here.

class Activity(models.Model):
    activity = models.TextField(null=True)
    accessibility= models.FloatField(max_length=255, null=True)
    type= models.TextField(null=True)
    participants = models.IntegerField(null=True)
    price = models.FloatField(max_length=255, null=True)
    link = models.TextField(null=True)
    key= models.IntegerField(primary_key=True)

    def __str__(self):
        return self.activity

  