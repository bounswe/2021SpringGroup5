from django.shortcuts import render   
from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def createEventPost(request):
    data=request.POST
    _,name,surname,username,id=data["actor"]
    _,kokok=data["object"]
    # İlgili event post verileir kullanılarak ve if ser.is_valid(): kullandıktan sonra dbye kaydet,
    # Offered badges'a da bir entry girilecek "badges": [ "inadequate_skill","good_teacher","friendly"] ve user_id kullanarak


    # .save() ledikten sonra state=status.HTTP_201_CREATED ile 
