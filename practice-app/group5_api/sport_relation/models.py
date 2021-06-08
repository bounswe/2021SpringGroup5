from django.db import models


class Sport(models.Model):
    link = models.CharField(max_length=2083, null=True)
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    id = models.IntegerField(primary_key=True)
    slug = models.CharField(max_length=255, null=True)
    icon = models.CharField(max_length=2083, null=True)
