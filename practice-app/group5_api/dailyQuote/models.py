from django.db import models


class DailyQuote(models.Model):
    quote_text = models.CharField(max_length=1000)  # quote text
    author = models.CharField(max_length=100)       # author of the quote
    date = models.DateField(unique=True)            # date of the quote
    points = models.IntegerField()                  # total points given
    ratings = models.IntegerField()                 # total ratings made
