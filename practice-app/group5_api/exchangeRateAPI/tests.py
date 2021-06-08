from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

import json

class UmutAPITests(APITestCase):

    #Test Post Method which add Category
    def test_add_category(self):
        client = APIClient()
        data = json.dumps({"category_name": "Soccer", "category_description": "Soccer description", "max_player": 100})
        response = client.generic('POST', '/exchangeRateAPI/add/category/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #Test Get Method which gets All Exchange Rates
    def test_get_all_currency(self):
        client = APIClient()
        response = client.get("/exchangeRateAPI/currency/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

     #Test Post Method which Calculator Exchange Rate and Insert it DB
    def test_add_current_currency_and_calculator(self):
        client = APIClient()
        data = json.dumps({"base_total": 10, "target_currency": "TRY"})
        response = client.generic('POST', '/exchangeRateAPI/add/currentCurrency/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #Test Get Method which gets All Event Posts
    def test_get_all_event_post(self):
        client = APIClient()
        response = client.get("/exchangeRateAPI/eventPost/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)