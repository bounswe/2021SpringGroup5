from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sportRelation/', include('sport_relation.urls')),
    path('dailyQuote/', include('dailyQuote.urls')),
    path('weatherCondition/',include('weatherCondition.urls')),
    path('nbaStats/', include('nbaStats.urls')),
    path('musicapi/',include('musicapi.urls')),
    path('exchangeRateAPI/', include('exchangeRateAPI.urls'))
]
