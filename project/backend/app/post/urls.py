from django.urls import path
from .views import EquipmentPostApi,CommentsApi

urlpatterns=[
    path('equipment_post/',EquipmentPostApi.as_view()),
    path('comment/',CommentsApi.as_view())
]