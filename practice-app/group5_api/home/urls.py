from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dailyQuote/', include('dailyQuote.urls')),
    path('weatherCondition/',include('weatherCondition.urls')),
    path('nbaStats/', include('nbaStats.urls'))
]
