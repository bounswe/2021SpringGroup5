from django.db import models
from django.contrib.auth.models import AbstractUser
from post.models import Sport


class User(AbstractUser):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    mail = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    location = models.CharField(max_length=50, null=True)


class InterestLevel(models.Model):
    owner_of_interest = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_level = models.ForeignKey('post.SkillLevel', null=True, on_delete=models.CASCADE)
    sport_name = models.ForeignKey('post.Sport', on_delete=models.CASCADE)

class Follow(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'following'], name='a user follows another user')
        ]
    follower=models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE,related_name='follower')
    following=models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE,related_name='following')
