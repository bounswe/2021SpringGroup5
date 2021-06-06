from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import requests

from myapp.models import Category
from myapp.models import EventPost
from myapp.models import CurrentCurrency

def index(request):
     return render(request, "index.html")

def get_category(request, category_name):
    if request.method == 'GET':
        try:
            category = Category.objects.get(name=category_name)
            response = json.dumps([{ 'Category': category.name, 'Description': category.description, 'Max Player': category.max_player}])
        except:
            response = json.dumps([{ 'Error': 'No category'}])
    return HttpResponse(response, content_type='text/json')

def get_all_category(request):
    if request.method == 'GET':
        try:
            list = []
            category_list = Category.objects.all()
            for category in category_list:
                response = json.dumps([{ 'Category': category.name, 'Description': category.description, 'Max Player': category.max_player}])
                list.append(response)
        except:
            response = json.dumps([{ 'Error': 'No category'}])
            list.append(response)
    return HttpResponse(list, content_type='text/json')


@csrf_exempt
def add_category(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        category_name = payload['category_name']
        category_description = payload['category_description']
        max_player = payload['max_player']
        category = Category(name=category_name, description=category_description, max_player=max_player)
        try:
            category.save()
            response = json.dumps([{ 'Success': 'Category added.'}])
        except:
            response = json.dumps([{ 'Error': 'Category could not be added.'}])
    return HttpResponse(response, content_type='text/json')

def get_event_post(request, post_id):
    if request.method == 'GET':
        try:
            post = EventPost.objects.get(event_post_id=post_id)
            response = json.dumps([{ 
                'Post ID': post.event_post_id, 
                'Date Time': post.date_time, 
                'Participation Limit': post.participation_limit, 
                'Spectator Limit': post.spectator_limit, 
                'Rule': post.rule, 
                'Equipment Requirement': post.equipment_requirement, 
                'Status': post.status, 
                'Location': post.location, 
                'Contact Info': post.contact_info, 
                'Skill Requirement': post.skill_requirement,
                'Repeating Frequency': post.repeating_frequency }])
        except:
            response = json.dumps([{ 'Error': 'No post'}])
    return HttpResponse(response, content_type='text/json')

def get_all_event_post(request):
    if request.method == 'GET':
        try:
            list = []
            post_list = EventPost.objects.all()
            for post in post_list:
                response = json.dumps([{ 
                    'Post ID': post.event_post_id, 
                    'Date Time': post.date_time, 
                    'Participation Limit': post.participation_limit, 
                    'Spectator Limit': post.spectator_limit, 
                    'Rule': post.rule, 
                    'Equipment Requirement': post.equipment_requirement, 
                    'Status': post.status, 
                    'Location': post.location, 
                    'Contact Info': post.contact_info, 
                    'Skill Requirement': post.skill_requirement,
                    'Repeating Frequency': post.repeating_frequency }])
                list.append(response)
        except:
            response = json.dumps([{ 'Error': 'No post'}])
            list.append(response)
    return HttpResponse(list, content_type='text/json')

@csrf_exempt
def add_event_post(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        event_post_id = payload['event_post_id']
        date_time = payload['date_time']
        participation_limit = payload['participation_limit']
        spectator_limit = payload['spectator_limit']
        rule = payload['rule']
        equipment_requirement = payload['equipment_requirement']
        status = payload['status']
        location = payload['location']
        contact_info = payload['contact_info']
        skill_requirement = payload['skill_requirement']
        repeating_frequency = payload['repeating_frequency']

        post = EventPost(event_post_id=event_post_id, date_time=date_time, participation_limit=participation_limit, spectator_limit=spectator_limit, rule=rule, equipment_requirement=equipment_requirement, status=status, location=location, contact_info=contact_info, skill_requirement=skill_requirement, repeating_frequency=repeating_frequency )
        try:
            post.save()
            response = json.dumps([{ 'Success': 'Event Post added.'}])
        except:
            response = json.dumps([{ 'Error': 'Event Post could not be added.'}])
    return HttpResponse(response, content_type='text/json')


def get_all_currency(request):
    if request.method == 'GET':
        try:
            list = []
            response = requests.get('https://openexchangerates.org/api/latest.json?app_id=9f85dc28cb9e43eb99dce0c859d49fc2')
            list.append(response.json())
        except:
            response = json.dumps([{ 'Error': 'No Currency'}])
            list.append(response)
    return HttpResponse(list, content_type='text/json')

def get_currency(request, target_currency):
    if request.method == 'GET':
        list = []
        try:
            response = requests.get('https://openexchangerates.org/api/latest.json?app_id=9f85dc28cb9e43eb99dce0c859d49fc2')
            responseJson = response.json()
            currencyList = responseJson['rates']
            currency = responseJson['rates'][target_currency]
            
            result = "1 USD = " + str(currency) + " " + target_currency
            response = json.dumps([{'Result': result}])
            list.append(response)
        except:
            response = json.dumps([{ 'Error': 'No Currency'}])
            list.append(response)
    return HttpResponse(list, content_type='text/json')

@csrf_exempt
def add_current_currency(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        base_total = payload['base_total']
        target_currency = payload['target_currency']

        response = requests.get('https://openexchangerates.org/api/latest.json?app_id=9f85dc28cb9e43eb99dce0c859d49fc2')
        responseJson = response.json()
        currencyList = responseJson['rates']
        currency = responseJson['rates'][target_currency]

        target_result = currency * float(base_total)
    
        base_currency = responseJson['base']

        currency = CurrentCurrency(base_currency=base_currency, base_total=base_total, target_currency=target_currency, target_result=target_result)
        list = []
        try:
            currency.save()
            result = str(base_total) + ' ' + base_currency + ' = ' + str("{:.2f}".format(target_result)) + ' ' + target_currency
            response = json.dumps([{ 'Success': 'Currenct currency added.', 'Result': result}])
        except:
            response = json.dumps([{ 'Error': 'Currenct currency could not be added.'}])
    return HttpResponse(response, content_type='text/json')
