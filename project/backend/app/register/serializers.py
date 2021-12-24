from django.db import models
from django.db.models import fields
from rest_framework import serializers
from register.models import User,InterestLevel,Follow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'surname', 'username', 'Id', 'mail', 'password', 'is_email_verified', 'location']

class InterestLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=InterestLevel
        fields='__all__'

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Follow
        fields='__all__'
