from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register, name='register_first'),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
    path("logout_user", views.logout_user, name='logout_user'),
    path('login', views.login_user, name='login'),
    path(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    path("me", views.profile, name='profile')
]