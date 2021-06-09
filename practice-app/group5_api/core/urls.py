
from django.contrib import admin
from django.urls import path, include
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('random/', views.showRandom, name='random'),
]
