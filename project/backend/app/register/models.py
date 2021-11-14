from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    mail = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    location = models.CharField(max_length=50, null=True)


class Sport(models.Model):
    sport_name = models.CharField(max_length=30, null=False)
    equipments = models.CharField(max_length=200)
    max_players = models.IntegerField(null=True)
    special_location = models.CharField(null=True, max_length=30)
    general_rules = models.CharField(null=True, max_length=300)


class InterestLevel(models.Model):
    owner_of_interest = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_level = models.CharField(max_length=30, null=True)
    sport_name = models.ForeignKey(Sport, on_delete=models.CASCADE)