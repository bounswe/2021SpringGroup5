from django.urls import path
from .views import musicapi, GetMusicView, get_music

urlpatterns = [
    path('', musicapi, name="musicapi"),
    path('musicAPI', GetMusicView.as_view(), name="musicAPI"),
    path('music', get_music, name="music"),
]
