from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class musicapi(APITestCase):

    # Test GET method
    def test_get_method(self):
        client = APIClient()
        response = client.get("/musicapi/api/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
