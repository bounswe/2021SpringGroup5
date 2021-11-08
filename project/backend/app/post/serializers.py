from django.db import models
from django.db.models import fields
from rest_framework import serializers
from post.models import BadgeOwnedByUser, EquipmentComment, EquipmentCommentActivtyStream, EventComment,\
    EventCommentActivtyStream, SkillLevel, Sport,EquipmentPost,EventPost,Application,Badge,BadgeOfferedByEventPost,EventPostActivityStream,\
    EquipmentPostActivtyStream


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

class SkillLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=SkillLevel
        fields='__all__'

class EventPostActivityStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventPostActivityStream
        fields='__all__'

class EquipmentPostActivtyStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model=EquipmentPostActivtyStream
        fields='__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Application
        fields='__all__'

class EventCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventComment
        fields='__all__'

class EquipmentCommentActivityStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model=EquipmentCommentActivtyStream
        fields='__all__'

class EventCommentActivityStreamSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventCommentActivtyStream
        fields='__all__'

class EquipmentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=EquipmentComment
        fields='__all__'

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Badge
        fields='__all__'

class BadgeOfferedByEventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BadgeOfferedByEventPost
        fields='__all__'

class BadgeOwnedByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=BadgeOwnedByUser
        fields='__all__'
