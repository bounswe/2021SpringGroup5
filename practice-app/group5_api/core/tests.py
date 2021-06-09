from django.test import TestCase
from randomActivity.models import Activity
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
# Create your tests here.

class randomPersonTest(APITestCase):


	#Test for get request
	def test_get_method(self):
		client = APIClient()
		response = client.get("core/api")
		self.assertEqual(response.status_code,status.HTTP_200_OK)
