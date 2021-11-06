from django.db import models

from django.contrib.auth.models import User # It will be changed once registiration module is done
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey 

# Create your models here.

class Sport(models.Model):
    sport_name=models.CharField(max_length=30,null=False,unique=True)
    equipments=models.TextField(null=True,blank=True,max_length=300)
    max_players=models.IntegerField(null=True,blank=True)
    special_location=models.CharField(null=True,blank=True,max_length=30)
    general_rules=models.TextField(null=True,blank=True,max_length=300)


class EquipmentPost(models.Model):
    post_name=models.CharField(null=False,blank=False,max_length=30)
    owner_id=models.ForeignKey(User,on_delete=models.CASCADE)
    sport_category_id=models.ForeignKey(Sport,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    description=models.TextField(max_length=300,null=False,blank=False)
    location=models.CharField(null=True,blank=True,max_length=200)
    link=models.URLField(null=True,blank=True)
    active=models.BooleanField(null=False,blank=False)
    pathToEquipmentPostImage=models.URLField()
    
class EventPost(models.Model):
    post_name=models.CharField(null=False,blank=False,max_length=30)
    owner_id=models.ForeignKey(User,on_delete=models.CASCADE)
    sport_category_id=models.ForeignKey(Sport,on_delete=models.CASCADE)
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
    pathToEventImage=models.URLField()

class SkillLevel(models.Model):
    level_name=models.CharField(null=False,blank=False,max_length=10, unique=True)

class EventPostSkillRequirements(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['event_post_id', 'level'], name='skill requirements for an event post')
        ]
    event_post_id=models.ForeignKey(EventPost,on_delete=CASCADE)
    level=models.ForeignKey(SkillLevel,on_delete=CASCADE)

class Application(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id', 'event_post_id'], name='application to an event post per user')
        ]
    user_id=models.ForeignKey(User,null=False,blank=False,on_delete=CASCADE)
    event_post_id=models.ForeignKey(EventPost,null=False,blank=False,on_delete=CASCADE)
    status=models.CharField(null=False,blank=False,max_length=8)
    applicant_type=models.CharField(null=False,blank=False,max_length=9)
    
class Comment(models.Model):
    content=models.TextField(max_length=300)
    owner_id=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    equipment_post_id=models.ForeignKey(EquipmentPost,null=True,blank=True,on_delete=models.CASCADE)
    event_post_id=models.ForeignKey(EventPost,null=True,blank=True,on_delete=models.CASCADE)

class Badge(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    description=models.TextField(max_length=300, null=True, blank=True)
    pathToBadgeImage=models.URLField()
    

class BadgeOfferedByEventPost(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['post_id', 'badge_id'], name='badge offered by an event post')
        ]
    post_id=ForeignKey(EventPost,on_delete=models.CASCADE)
    badge_id=ForeignKey(Badge,on_delete=models.CASCADE)

class BadgeOwnedByUser(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner_id', 'badge_id'], name='badge owned by a user')
        ]
    badge_id=models.ForeignKey(Badge,on_delete=CASCADE)
    owner_id=models.ForeignKey(User, on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now_add=True)
    isGivenBySystem=models.BooleanField()