from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import PersonSerializer
from .models import Person
import requests

# Create your views here.


def home(request):
    count = User.objects.count()
    return render(request, 'core/home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {
        'form': form
    })


def showRandom(request):
    response = requests.get('https://randomuser.me/api/')
    randomUser = response.json()
    return render(request, 'core/random.html', {
        'name': randomUser['results'][0]['name']['first'],
        'surname': randomUser['results'][0]['name']['last'],
        'gender': randomUser['results'][0]['gender'],
        'age': randomUser['results'][0]['dob']['age'],

    })
