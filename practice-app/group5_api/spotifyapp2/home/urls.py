
from django.urls import path
from .views import home, GetMusicView, get_music

urlpatterns = [
    path('', home, name="home"),
    path('musicAPI', GetMusicView.as_view(), name="musicAPI"),
    path('music', get_music, name="music"),
]
