from django.urls import path
from search import views

urlpatterns=[
    path('search_event/',views.searchEvent,name='searches an event post'),
    path('search_equipment/',views.searchEquipment,name='searches an equipment post')
]