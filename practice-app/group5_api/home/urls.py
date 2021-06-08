from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sportRelation/', include('sport_relation.urls'))
]
