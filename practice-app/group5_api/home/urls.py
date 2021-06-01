from django.urls import path,include

from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weatherCondition/',include('weatherCondition.urls'))
]