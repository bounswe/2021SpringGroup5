"""group5_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from exchangeRateAPI import views

# Manage URL Patterns

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('', views.index),
    path('add/category/', views.add_category),
    path('category/', views.get_all_category),
    path('category/all/', views.get_all_category),
    path('category/<str:category_name>/', views.get_category),

    path('add/eventPost/', views.add_event_post),
    path('eventPost/', views.get_all_event_post),
    path('eventPost/all/', views.get_all_event_post),
    path('eventPost/<int:post_id>/', views.get_event_post),

    path('currency/', views.get_all_currency),
    path('currency/all/', views.get_all_currency),
    path('currency/<str:target_currency>/', views.get_currency),
    path('add/currentCurrency/', views.add_current_currency),

]

