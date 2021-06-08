from django.db import models

#Create Category Table which has name, description and max_player fields
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    max_player = models.IntegerField()

#Create EventPost Table which has below fields
class EventPost(models.Model):
    event_post_id = models.IntegerField()
    date_time = models.CharField(max_length=100)
    participation_limit = models.IntegerField()
    spectator_limit = models.IntegerField()
    rule = models.CharField(max_length=100)
    equipment_requirement = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    skill_requirement = models.CharField(max_length=100)
    repeating_frequency = models.IntegerField()

#Create CurrentCurrency Table which has below fields
class CurrentCurrency(models.Model):
    base_currency = models.CharField(max_length=100)
    base_total = models.IntegerField()
    target_currency = models.CharField(max_length=100)
    target_result = models.IntegerField()