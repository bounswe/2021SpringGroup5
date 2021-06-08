from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_quote, name='show_quote'),
    path('api/', views.quote_api, name='quote_api'),
]