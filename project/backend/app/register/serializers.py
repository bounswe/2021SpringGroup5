from django.db import models
from django.db.models import fields
from rest_framework import serializers
from register.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'surname', 'username', 'Id', 'mail', 'password', 'is_email_verified', 'location']
