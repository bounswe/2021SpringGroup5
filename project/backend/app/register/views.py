import threading
from django.forms.models import model_to_dict
import requests
from django.shortcuts import render, redirect
from requests import api
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.backends import TokenBackend
from django.contrib.auth.decorators import login_required
from .models import User, InterestLevel, Follow
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
SkillLevel = apps.get_model('post', 'SkillLevel')
EquipmentPost = apps.get_model('post', 'EquipmentPost')
BadgeOwnedByUser = apps.get_model('post', 'BadgeOwnedByUser')
EventPost = apps.get_model('post', 'EventPost')

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


@login_required
@api_view(['GET'])
def homePageEvents(request):
    actor_id = request.user.Id

    following_user_ids = list(Follow.objects.filter(follower=actor_id).values('following__Id'))

    if len(following_user_ids) == 0:
        return Response({"message": "No record found"}, 404)

    result_events = []
    for i in range(len(following_user_ids)):
        try:
            event = model_to_dict(
                EventPost.objects.filter(owner=following_user_ids[i]["following__Id"], status='upcoming').last())

            sport_name = Sport.objects.get(id=event["sport_category"]).sport_name
            event["sport_category"] = sport_name
            event["skill_requirement"] = SkillLevel.objects.get(pk=event["skill_requirement"]).level_name
            result_events.append(event)
        except:
            continue

    return Response({"posts": result_events}, 200)


@login_required
@api_view(['GET'])
def getBadgesOwnedByUser(request):
    actor_id = request.user.Id
    try:
        badges = list(
            BadgeOwnedByUser.objects.filter(owner=actor_id).values('badge__id', 'badge__name', 'badge__description',
                                                                   'badge__wikiId'))
        return Response({"badges": badges}, 200)
    except:
        return Response({"message": "This user has not received any badges"}, 404)


@api_view(['GET', 'POST'])
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
        send_mail(user, request)
        skill1 = SkillLevel.objects.get(level_name=level1)
        skill2 = SkillLevel.objects.get(level_name=level2)

        sport1 = Sport.objects.get(sport_name=interest1)
        sport2 = Sport.objects.get(sport_name=interest2)

        interest1 = InterestLevel.objects.create(owner_of_interest=user, sport_name=sport1, skill_level=skill1)
        interest2 = InterestLevel.objects.create(owner_of_interest=user, sport_name=sport2, skill_level=skill2)

        interest1.save()
        interest2.save()

        user.set_password(password)
        user.save()

        return Response('SUCCESS', status=status.HTTP_201_CREATED)
    else:
        sports = list(Sport.objects.filter(is_custom=False).values('id', "sport_name"))
        skill_levels = list(SkillLevel.objects.values())
        res = {"sports": sports, "skill_levels": skill_levels}
        return Response(res, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
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
        postjson = {
            'username': username,
            'password': password
        }

        token = requests.post("http://3.122.41.188:8000/api/token/", json=postjson)

        return Response(token.json(), status=status.HTTP_200_OK)
    else:
        return Response({"message": "You are not logged in, you can't do this request"}, 401)


@login_required()
@api_view(['GET'])
def profile(request):
    user = request.user
    context = {
        'username': user.username,
        'name': user.name,
        'mail': user.mail,
        'Id': user.Id,
        'surname': user.surname,
        'location': user.location
    }
    return Response(context, status=status.HTTP_200_OK)


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


@login_required()
@api_view(['POST'])
def follow(request, userId):
    followinguser = request.user
    followeduser = User.objects.get(Id=userId)

    Follow.objects.create(follower=followinguser, following=followeduser)

    return JsonResponse('SUCCESS', status=201)



@login_required()
@api_view(['GET'])
def getProfileOfUser(request, userId):
    user1 = request.user
    user2 = User.objects.get(Id=userId)

    badges = list(
        BadgeOwnedByUser.objects.filter(owner=user2.Id).values('badge__id', 'badge__name', 'badge__description',
                                                               'badge__wikiId'))
    events = list(EventPost.objects.filter(owner=user2.Id).values())
    equipments = list(EquipmentPost.objects.filter(owner=user2).values())
    sports = list(InterestLevel.objects.filter(owner_of_interest=user2).values())
    user = list(
        User.objects.filter(username=user2.username).values('username', 'name', 'surname', 'location')).__getitem__(0)
    try:
        follow = Follow.objects.get(follower=user1, following=user2)
        following = True
    except:
        following = False
    context = {
        'badges': badges,
        'equipments': equipments,
        'events': events,
        'sports': sports,
        'user': user,
        'following': following,
    }
    return JsonResponse(context, status=200)
  
