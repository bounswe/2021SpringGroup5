from django.shortcuts import render
from rest_framework.decorators import api_view
import requests
from .models import DailyQuote
from .serializer import DailyQuoteSerializer
from rest_framework.response import Response
from rest_framework import status as s
from datetime import datetime


def quote():
    today = str(datetime.utcnow().date())
    points, ratings, value = 0, 0 , 0

    # get the quote with todays date from the database, if exists
    try:
        quote_in_db = DailyQuoteSerializer(DailyQuote.objects.filter(date=today)[0]).data
    except:
        quote_in_db = None

    # if the quote of today has been saved before, take the points and ratings
    if quote_in_db is not None:
        points = quote_in_db["points"]
        ratings = quote_in_db["ratings"]

    # send get request to the remote api
    api = 'https://quotes.rest/qod?category=sports&language=en'
    response = requests.get(api)

    # if the response is successful, process the response of the remote api
    if response.status_code == 200:
        res = response.json()["contents"]["quotes"][0]
        res["quote_text"] = res['quote']
    # due to request limit per hour, the response may return 429, too many requests
    # if so, process the response of the database
    else:
        res = quote_in_db

    # make sure that the res is not None
    # it can be None if the remote api did not return 200 and the database is empty
    if res is not None:
        quote_text = res["quote_text"]
        author = res["author"]
        date = res["date"]
        # if there is not a row in the database for today, create a new object and save it to the database
        if quote_in_db is None:
            new_quote = DailyQuote(quote_text=quote_text, author=author, date=date,
                                   points=0, ratings=0)
            new_quote.save()
            status = s.HTTP_201_CREATED

        # if there exists a row in the database for today, then calculate the value to be shown
        else:
            if not ratings == 0:
                value = points * 1.0 / ratings
                value = "{:.1f}".format(value)
            status = s.HTTP_200_OK

        # send quote text, author, calculated value and number of ratings as the response
        dictionary = {"quote_text": quote_text, "author": author, "value": value, "ratings": ratings}

    # if res is None (the remote api did not return 200 and the database is empty), return 404
    else:
        dictionary = False
        status = s.HTTP_404_NOT_FOUND

    return Response({"response": dictionary}, status=status)


def rate(points):

    # make sure that the input is valid, if not, return 400
    if points is None or (not str(points).isdecimal()) or (not int(points) in [0, 1, 2, 3, 4, 5]):
        dictionary = False
        status = s.HTTP_400_BAD_REQUEST
        return Response({"response": dictionary}, status=status)

    today = str(datetime.utcnow().date())
    # if somebody has rated, the quote they liked is today's quote, which is in the database
    try:
        quote_in_db = DailyQuoteSerializer(DailyQuote.objects.filter(date=today)[0]).data
    except:
        quote_in_db = None

    # if we could get the row from the database successfully, process it
    if quote_in_db is not None:
        points = int(points)
        # calculate points, ratings and value
        points_total = quote_in_db["points"] + points
        ratings_total = quote_in_db["ratings"] + 1
        value = points_total * 1.0 / ratings_total
        value = "{:.1f}".format(value)
        dictionary = {"quote_text": quote_in_db["quote_text"],
                      "author": quote_in_db["author"],
                      "value": value,
                      "ratings": ratings_total}
        DailyQuote.objects.filter(date=quote_in_db["date"]).update(points=points_total)
        DailyQuote.objects.filter(date=quote_in_db["date"]).update(ratings=ratings_total)
        status = s.HTTP_200_OK

    # if we could not get the row from the database successfully (unlikely) return 404
    else:
        dictionary = False
        status = s.HTTP_404_NOT_FOUND

    return Response({"response": dictionary}, status=status)


@api_view(['GET', 'POST'])
def show_quote(request):
    if request.method == 'GET':
        res = quote().data
        return render(request, 'dailyQuote/base.html', res)
    else:
        res = rate(request.POST.get("Points", '')).data
        return render(request, 'dailyQuote/base.html', res)


@api_view(['GET', 'POST'])
def quote_api(request):
    if request.method == 'GET':
        res = quote()
        return res
    else:
        res = rate(request.POST.get("Points", ''))
        return res
