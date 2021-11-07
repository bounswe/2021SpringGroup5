from django.urls import path
from post import views

urlpatterns=[
    path('create_event_post/',views.createEventPost,name='create an event post'),
    path('create_equipment_post/',views.createEquipmentPost,name='create an equipment post'),
]