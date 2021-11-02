from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register_first, name='register_first'),
    path('register_second', views.register_second, name='register_second'),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
    path("logout_user", views.logout_user, name='logout_user'),
    path('home', views.home, name='home'),

]