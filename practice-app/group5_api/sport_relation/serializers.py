from .models import Sport
from rest_framework import serializers


class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields = ['id', 'name', 'description',
                  'link', 'slug', 'icon']
