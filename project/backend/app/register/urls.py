from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('register', views.register, name='register_first'),
    path('activate-user/<uidb64>/<token>',
         views.activate_user, name='activate'),
    path("logout_user", views.logout_user, name='logout_user'),
    path('login', views.login_user, name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]