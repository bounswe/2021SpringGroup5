from django.urls import path

from weatherCondition import views

urlpatterns = [
    path('', views.index, name='index'),
]