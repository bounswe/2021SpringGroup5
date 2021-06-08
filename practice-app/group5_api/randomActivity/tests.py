from django.test import TestCase
from randomActivity.models import Activity
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
# Create your tests here.

class RandomActivity(APITestCase):

    # Tests if the get request works
    def test_get_method(self):
        client=APIClient()
        response=client.get("/randomActivity/api/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
