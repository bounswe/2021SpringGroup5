from .serializers import SportSerializer
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, mixins, generics
import requests
from .models import Sport
from django.urls import reverse


base_url = 'https://sports.api.decathlon.com/sports/'


class SportDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


def get_related_sports(pk):
    url = base_url + str(pk)
    try:
        sports = requests.get(url).json()
        # if there is not any related sport (in this case decathlon api will not return a list for related field)
        if not isinstance(sports['data']['relationships']['related'], list):
            return []

        return [{
                **SportSerializer(Sport.objects.get(pk=x['data']['id'])).data,
                'weight': float(x['data']['weight'])
                } for x in sports['data']['relationships']['related']]
    except:
        return False


class SimilarSport(APIView):

    def get(self, request, pk):
        related_sports = get_related_sports(pk)

        if related_sports == False:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        if len(related_sports) > 5:
            return Response(related_sports[:5])

        return Response(related_sports)


class SuggestSport(APIView):

    def get(self, request, arg):
        pks = arg.split('-')
        suggestions = {}

        for pk in pks:

            related_sports = get_related_sports(pk)

            if related_sports == False:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

            for sport in related_sports:

                if sport['id'] in pks:  # we are looking for sports which are not choosen by user
                    continue

                # if we encounter with that sport before, update its weight
                if suggestions.get(sport['id']):
                    suggestions[sport['id']]['weight'] += sport['weight']
                else:  # if it is the first time we are encountering with that sport
                    suggestions[sport['id']] = sport

        suggestion = {}
        if suggestions:
            suggestion = max(suggestions.values(), key=lambda x: x['weight'])

        return Response(suggestion)


class SaveSportListScript(APIView):
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        url = base_url
        response = requests.get(url)
        sportlist = response.json()['data']

        sportlist = [{
            'link': x['links']['self'],
            'name': x['attributes']['name'],
            'description': x['attributes']['description'],
            'id': x['id'],
            'slug': x['attributes']['slug'],
            'icon': x['attributes']['icon'],
        } for x in sportlist]

        ids = []

        for sport in sportlist:
            serializer = SportSerializer(data=sport)
            if serializer.is_valid():
                serializer.save()
                ids.append(sport['id'])
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'AcceptedIds': ids}, status=status.HTTP_201_CREATED)


def get_api_url(url):
    return '/'.join(url.split('/')[:-1]) + "/api/"


def index(request):
    sportlist = Sport.objects.order_by('name')

    context = {
        'sportlist': sportlist
    }

    return render(request, 'sport_relation/index.html', context)


def similar(request):
    api_url = get_api_url(request.build_absolute_uri())
    pk = request.GET.get('sportlist', False)
    url = api_url + "similar/" + pk

    similar_sports = requests.get(url).json()
    root_sport = Sport.objects.get(pk=pk)

    context = {
        "similar_sports": similar_sports,
        "root_sport": root_sport
    }

    return render(request, 'sport_relation/similar.html', context)


def suggest(request):
    api_url = get_api_url(request.build_absolute_uri())
    pks = [request.GET.get('sportlist1', False), request.GET.get(
        'sportlist2', False), request.GET.get('sportlist3', False)]
    url = api_url + "suggest/" + "-".join(pks)

    suggestion = requests.get(url).json()
    root_sports = [Sport.objects.get(pk=pk) for pk in pks]

    context = {
        "suggestion": suggestion,
        "root_sports": root_sports
    }

    return render(request, 'sport_relation/suggest.html', context)
