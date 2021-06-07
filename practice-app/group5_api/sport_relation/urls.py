from django.urls import path
from . import views

app_name = 'sport_relation'

urlpatterns = [
    path('api/similar/<int:pk>', views.SimilarSport.as_view(), name="api-similar"),
    path('api/sports/<int:pk>', views.SportDetail.as_view(), name="api-sports"),
    path('api/suggest/<str:arg>', views.SuggestSport.as_view(), name="api-suggest"),
    path('api/save-sport-list-script', views.SaveSportListScript.as_view(),
         name="api-save-sport-list-script"),

    path('', views.index, name="index"),
    path('similar', views.similar, name="similar"),
    path('suggest', views.suggest, name="suggest")

]
