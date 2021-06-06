from .models import Activity
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ['activity', 'accessibility', 'type',
                  'participants', 'price', 'link', 'key']
