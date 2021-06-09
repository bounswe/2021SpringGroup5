from django.urls import path

from . import views

urlpatterns = [

    path('', views.stats_api, name='home')

]
