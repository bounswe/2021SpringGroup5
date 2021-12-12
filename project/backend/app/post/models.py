import uuid
from typing import Callable
from django.db import models
from django.contrib import admin
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.

class Sport(models.Model):
    sport_name=models.CharField(max_length=70,null=False,unique=True)
    is_custom=models.BooleanField(null=False,blank=False)


class EquipmentPost(models.Model):
    post_name=models.CharField(null=False,blank=False,max_length=30)
    owner=models.ForeignKey('register.User',on_delete=models.CASCADE)
    sport_category=models.ForeignKey(Sport,on_delete=models.CASCADE)
    created_date=models.DateTimeField(null=False,blank=False,default=timezone.now)
    description=models.TextField(max_length=300,null=False,blank=False)
    longitude=models.FloatField(null=True,blank=True)
    latitude=models.FloatField(null=True,blank=True)
    link=models.URLField(null=True,blank=True)
    active=models.BooleanField(null=False,blank=False)
    pathToEquipmentPostImage=models.URLField(null=True,blank=True)


class SkillLevel(models.Model):
    level_name=models.CharField(null=False,blank=False,max_length=10, unique=True)
    
class EventPost(models.Model):
    post_name=models.CharField(null=False,blank=False,max_length=30)
    owner=models.ForeignKey('register.User',on_delete=models.CASCADE,to_field='Id')
    sport_category=models.ForeignKey(Sport,on_delete=models.CASCADE)
    created_date=models.DateTimeField(null=False,blank=False,default=timezone.now)
    description=models.TextField(max_length=300,null=False,blank=False)
    longitude=models.FloatField(null=True,blank=True)
    latitude=models.FloatField(null=True,blank=True)
    date_time=models.DateTimeField(null=False,blank=False)
    participant_limit=models.IntegerField(null=False,blank=False)
    spectator_limit=models.IntegerField(null=False,blank=False)
    rule=models.TextField(null=False,blank=False,max_length=300)
    equipment_requirement=models.TextField(null=True,blank=True,max_length=300)
    status=models.CharField(null=False,blank=False,max_length=10)
    capacity=models.CharField(null=False,blank=False,max_length=25)
    location_requirement=models.CharField(null=True,blank=True,max_length=30)
    contact_info=models.CharField(null=True,blank=True,max_length=50)
    pathToEventImage=models.URLField(null=True,blank=True)
    skill_requirement=models.ForeignKey(SkillLevel,on_delete=CASCADE)



class EventPostActivityStream(models.Model):
    context=models.URLField(null=False,blank=False) 
    summary=models.CharField(max_length=200,null=False,blank=False)
    actor=models.ForeignKey('register.User',on_delete=CASCADE)
    type=models.CharField(max_length=20,null=False,blank=False)
    object=models.ForeignKey(EventPost,on_delete=CASCADE)

class EquipmentPostActivtyStream(models.Model):
    context=models.URLField(null=False,blank=False) 
    summary=models.CharField(max_length=200,null=False,blank=False)
    actor=models.ForeignKey('register.User',on_delete=CASCADE)
    type=models.CharField(max_length=20,null=False,blank=False)
    object=models.ForeignKey(EquipmentPost,on_delete=CASCADE)


class Application(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'event_post'], name='application to an event post per user')
        ]
    user=models.ForeignKey('register.User',null=False,blank=False,on_delete=CASCADE)
    event_post=models.ForeignKey(EventPost,null=False,blank=False,on_delete=CASCADE)
    status=models.CharField(null=False,blank=False,max_length=10)
    applicant_type=models.CharField(null=False,blank=False,max_length=20)
    

class EventComment(models.Model):
    content=models.TextField(max_length=300)
    owner=models.ForeignKey('register.User',on_delete=models.CASCADE)
    created_date=models.DateTimeField(null=False,blank=False,default=timezone.now)
    event_post=models.ForeignKey(EventPost,null=True,blank=True,on_delete=models.CASCADE)

class EventCommentActivtyStream(models.Model):
    object=models.ForeignKey(EventComment,on_delete=CASCADE)
    context=models.URLField(null=False,blank=False) #????????????
    summary=models.CharField(max_length=200,null=False,blank=False)
    actor=models.ForeignKey('register.User',on_delete=CASCADE)
    type=models.CharField(max_length=20,null=False,blank=False)

class EquipmentComment(models.Model):
    content=models.TextField(max_length=300)
    owner=models.ForeignKey('register.User',on_delete=models.CASCADE)
    created_date=models.DateTimeField(null=False,blank=False,default=timezone.now)
    equipment_post=models.ForeignKey(EquipmentPost,null=True,blank=True,on_delete=models.CASCADE)

class EquipmentCommentActivtyStream(models.Model):
    object=models.ForeignKey(EquipmentComment,on_delete=CASCADE)
    context=models.URLField(null=False,blank=False) #????????????
    summary=models.CharField(max_length=200,null=False,blank=False)
    actor=models.ForeignKey('register.User',on_delete=CASCADE)
    type=models.CharField(max_length=20,null=False,blank=False)

class Badge(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(max_length=300, null=True, blank=True)
    pathToBadgeImage=models.URLField(null=True,blank=True)
    

class BadgeOfferedByEventPost(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post', 'badge'], name='badge offered by an event post')
        ]
    post=models.ForeignKey(EventPost,on_delete=models.CASCADE)
    badge=models.ForeignKey(Badge,on_delete=models.CASCADE)

class BadgeOwnedByUser(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner', 'badge'], name='badge owned by a user')
        ]
    badge=models.ForeignKey(Badge,on_delete=CASCADE)
    owner=models.ForeignKey('register.User', on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now_add=True)
    isGivenBySystem=models.BooleanField()
