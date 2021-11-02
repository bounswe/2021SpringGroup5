from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    mail = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
