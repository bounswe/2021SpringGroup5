from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.TextField(null=True)
	surname = models.TextField(null=True)
	gender = models.TextField(null=True)
	age = models.IntegerField()