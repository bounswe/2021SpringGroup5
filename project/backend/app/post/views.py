from django.db.models.query import QuerySet
from django.shortcuts import render
from project.backend.app.post.models import EquipmentPost, Comment
from rest_framework.views import APIView
from rest_framework import status, permissions, mixins, generics
import requests
from .serializers import CommentSerializer, EquipmentPostSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.
    

class EquipmentPostApi(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.CreateModelMixin,
    mixins.UpdateModelMixin,mixins.DeleteModelMixin):

    serializer_class=EquipmentPostSerializer
    queryset=EquipmentPost.objects.all()
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

class CommentsApi(generics.GenericAPIView, mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DeleteModelMixin):

    serializer_class=CommentSerializer
    queryset= Comment.objects.all()
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)