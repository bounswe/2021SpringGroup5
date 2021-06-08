from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_page),
    path('api/pollution/', views.get_pollution),
    path('api/locations/', views.location_list),
]