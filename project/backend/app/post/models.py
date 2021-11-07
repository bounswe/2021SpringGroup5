from typing import Callable
from django.db import models

from django.contrib.auth.models import User # It will be changed once registiration module is done
from django.db.models.deletion import CASCADE

# Create your models here.

class Sport(models.Model):
    sport_name=models.CharField(max_length=30,null=False,unique=True)


class EquipmentPost(models.Model):
    post_name=models.CharField(null=False,blank=False,max_length=30)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    sport_category=models.ForeignKey(Sport,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    description=models.TextField(max_length=300,null=False,blank=False)
    location=models.CharField(null=True,blank=True,max_length=200)
    link=models.URLField(null=True,blank=True)
    active=models.BooleanField(null=False,blank=False)
    pathToEquipmentPostImage=models.URLField(null=True,blank=True)
    
class EventPost(models.Model):
    post_name=models.CharField(null=False,blank=False,max_length=30)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    sport_category=models.ForeignKey(Sport,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    description=models.TextField(max_length=300,null=False,blank=False)
    location=models.CharField(null=True,blank=True,max_length=200)
    date_time=models.DateTimeField(null=False,blank=False)
    participant_limit=models.IntegerField(null=False,blank=False)
    spectator_limit=models.IntegerField(null=False,blank=False)
    rule=models.TextField(null=False,blank=False,max_length=300)
    equipment_requirement=models.TextField(null=False,blank=False,max_length=300)
    status=models.CharField(null=False,blank=False,max_length=10)
    capacity=models.CharField(null=False,blank=False,max_length=25)
    location_requirement=models.CharField(null=True,blank=True,max_length=30)
    contact_info=models.CharField(null=True,blank=True,max_length=50)
    repeating_frequency=models.IntegerField(null=False,blank=False)
    pathToEventImage=models.URLField(null=True,blank=True)

class EventPostActivityStream(models.Model):
    context=models.URLField(null=False,blank=False) #????????????
    summary=models.CharField(max_length=200,null=False,blank=False)
    actor=models.ForeignKey(User,on_delete=CASCADE)
    type=models.CharField(max_length=20,null=False,blank=False)
    object=models.ForeignKey(EventPost,on_delete=CASCADE)

class EquipmentPostActivtyStream(models.Model):
    context=models.URLField(null=False,blank=False) #????????????
    summary=models.CharField(max_length=200,null=False,blank=False)
    actor=models.ForeignKey(User,on_delete=CASCADE)
    type=models.CharField(max_length=20,null=False,blank=False)
    object=models.ForeignKey(EquipmentPost,on_delete=CASCADE)

class SkillLevel(models.Model):
    level_name=models.CharField(null=False,blank=False,max_length=10, unique=True)

class EventPostSkillRequirements(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['event_post', 'level'], name='skill requirements for an event post')
        ]
    event_post=models.ForeignKey(EventPost,on_delete=CASCADE)
    level=models.ForeignKey(SkillLevel,on_delete=CASCADE)

class Application(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'event_post'], name='application to an event post per user')
        ]
    user=models.ForeignKey(User,null=False,blank=False,on_delete=CASCADE)
    event_post=models.ForeignKey(EventPost,null=False,blank=False,on_delete=CASCADE)
    status=models.CharField(null=False,blank=False,max_length=8)
    applicant_type=models.CharField(null=False,blank=False,max_length=9)
    
class EventComment(models.Model):
    content=models.TextField(max_length=300)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    event_post=models.ForeignKey(EventPost,null=True,blank=True,on_delete=models.CASCADE)

class EventCommentActivtyStream(models.Model):
    object=models.ForeignKey(EventComment,on_delete=CASCADE)
    context=models.URLField(null=False,blank=False) #????????????
    summary=models.CharField(max_length=200,null=False,blank=False)
    actor=models.ForeignKey(User,on_delete=CASCADE)
    type=models.CharField(max_length=20,null=False,blank=False)

class EquipmentComment(models.Model):
    content=models.TextField(max_length=300)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    equipment_post=models.ForeignKey(EquipmentPost,null=True,blank=True,on_delete=models.CASCADE)

class EquipmentCommentActivtyStream(models.Model):
    object=models.ForeignKey(EquipmentComment,on_delete=CASCADE)
    context=models.URLField(null=False,blank=False) #????????????
    summary=models.CharField(max_length=200,null=False,blank=False)
    actor=models.ForeignKey(User,on_delete=CASCADE)
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
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now_add=True)
    isGivenBySystem=models.BooleanField()

