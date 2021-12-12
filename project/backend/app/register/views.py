import threading

import requests
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from .models import User, InterestLevel
from django.urls import reverse
import hashlib
from django.http import JsonResponse
from django.contrib import messages
from django.template.loader import render_to_string
from .utils import generate_token
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings
from rest_framework.decorators import api_view

from django.apps import apps
Sport = apps.get_model('post', 'Sport')
SkillLevel=apps.get_model('post','SkillLevel')

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_mail(user, request):
    current_site = get_current_site(request)
    mail_subject = 'Complete Your Login'
    mail_body = render_to_string('verification/activate.html', {
        'username': user.username,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=mail_subject, body=mail_body,
                         from_email=settings.EMAIL_HOST_USER,
                         to=[user.mail])
    email.send(fail_silently=False)


@api_view(['GET','POST'])
@csrf_exempt
def register(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        context = body['actor']

        mail = context['email']
        name = context['name']
        surname = context['surname']
        password = context['password1']
        password2 = context['password2']
        username = context['username']
        interest1 = body['items'][0]['name']
        interest2 = body['items'][1]['name']
        level1 = body['items'][0]['level']
        level2 = body['items'][1]['level']

        if User.objects.filter(username=username).exists():
            context['errormessage'] = 'Username is taken, choose another one'
            context['has_error'] = True

            return JsonResponse(context, status=409)

        if User.objects.filter(mail=mail).exists():
            context['errormessage'] = 'This mail address is already in use'
            context['has_error'] = True

            return JsonResponse(context, status=409)

        if password != password2:
            context['errormessage'] = 'Passwords are not equal, please try again'
            context['has_error'] = True

            return JsonResponse(context, status=401)
        if len(username) < 8:
            context['errormessage'] = 'Username must have at least 8 characters'
            context['has_error'] = True

            return JsonResponse(context, status=401)

        user = User.objects.create_user(username=username, mail=mail, name=name, surname=surname)
        user.set_password(password)
        user.save()

        send_mail(user, request)

        sport1 = Sport.objects.get(sport_name=interest1)
        sport2 = Sport.objects.get(sport_name=interest2)

        interest1 = InterestLevel.objects.create(owner_of_interest=user, sport_name=sport1, skill_level=level1)
        interest2 = InterestLevel.objects.create(owner_of_interest=user, sport_name=sport2, skill_level=level2)

        interest1.save()
        interest2.save()

        return Response('SUCCESS', status=status.HTTP_200_OK)
    else:
        sports=list(Sport.objects.filter(is_custom=False).values('id',"sport_name"))
        skill_levels=list(SkillLevel.objects.values())
        res={"sports":sports,"skill_levels":skill_levels}
        return Response(res,status=status.HTTP_200_OK)


@api_view(['GET','POST'])
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        context = body['actor']

        username = context['username']
        password = context['password']

        user = authenticate(username=username, password=password)

        if user and not user.is_email_verified:
            context['errormessage'] = 'Please check your email inbox, your email is not verified'
            context['has_error'] = True
            return JsonResponse(context)

        if not user:
            context['errormessage'] = 'You entered invalid credentials, try again please'
            context['has_error'] = True
            return JsonResponse(context)

        login(request, user)

        return Response('SUCCESS', status=status.HTTP_200_OK)
    else:
        return Response({"message":"You are not logged in, you can't do this request"},401)



@api_view(['POST'])
def logout_user(request):
    logout(request)

    context = {'has_error': False}
    return JsonResponse(context)


@api_view(['GET'])
def activate_user(request, uidb64, token):
    context = {'has_error': False, 'message': ''}
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        context['message'] = 'Email verified, you can now login'
        return JsonResponse(context)

    context['has_error'] = True
    context['message'] = 'There is a problem with activation'
    return JsonResponse(context)
