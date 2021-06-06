from django.urls import path

from weatherCondition import views

urlpatterns = [
    path('api/', views.weather_api, name='weather_api'),
    path('', views.showWeather, name='showWeather'),
]