from django.urls import path
from post import views

urlpatterns=[
    path('create_equipment_post/',views.createEventPost,name='create an event post'),
]