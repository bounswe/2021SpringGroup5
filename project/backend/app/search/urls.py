from django.urls import path
from search import views

urlpatterns=[
    path('search_event/',views.searchEvent,name='create an event post')
]