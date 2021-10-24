from django.db import models
from django.db.models import fields
from rest_framework import serializers
from post.models import Sport,Post,EquipmentPost,EventPost,Comment

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sport
        fields=['id','sport_name','equipments','max_players','special_location','general_rules']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','post_name','owner_id','type_of_sport_id','created_date','description','location']

class EquipmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=EquipmentPost
        fields='__all__'

"""class EventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventPost
        fields='__all__'"""

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'