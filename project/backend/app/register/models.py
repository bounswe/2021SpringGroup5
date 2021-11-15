from django.db import models
from django.contrib.auth.models import AbstractUser
from post.models import Sport


class User(AbstractUser):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    mail = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    location = models.CharField(max_length=50, null=True)


class InterestLevel(models.Model):
    owner_of_interest = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_level = models.CharField(max_length=30, null=True)
    sport_name = models.ForeignKey('post.Sport', on_delete=models.CASCADE)
