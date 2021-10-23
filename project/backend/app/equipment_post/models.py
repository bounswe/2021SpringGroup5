from django.db import models
from django.contrib.auth.models import User # It will be changed once registiration module is done

# Create your models here.

class Sport(models.Model):
    sport_name=models.CharField(max_length=30,null=False)
    equipments=models.CharField(max_length=200)
    max_players=models.IntegerField(null=True)
    special_location=models.CharField(null=True,max_length=30)
    general_rules=models.CharField(null=True,max_length=300)


class Post(models.Model):
    name=models.CharField(null=False,blank=False,max_length=30)
    owner_id=models.ForeignKey(User,on_delete=models.CASCADE)
    type_of_sport=models.ForeignKey(Sport,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    description=models.CharField(max_length=200,null=False)
    location=models.CharField(null=True,blank=True,max_length=200)

class EquipmentPost(Post):
    
    link=models.CharField(null=True,blank=True)
    active=models.BooleanField(null=False)
    
class EquipmentComments(models.Model):
    content=models.CharField(max_length=300)
    owner_id=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    

