from django.db import models
from django.db.models import fields
from rest_framework import serializers
from post.models import Sport,EquipmentPost,EventPost,Application,Badge,BadgeOfferedByEventPost

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sport
        fields='__all__'

class EquipmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=EquipmentPost
        fields='__all__'

class EventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventPost
        fields='__all__'



class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields='__all__'

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Badge
        fields='__all__'

class BadgeOfferedByEventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BadgeOfferedByEventPost
        fields='__all__'