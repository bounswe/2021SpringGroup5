from .models import Person
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):

	class Meta:
		model = Person
		fields = ['name', 'surname', 'gender', 'age']