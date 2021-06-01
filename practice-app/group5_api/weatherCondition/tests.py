from weatherCondition.models import WeatherCondition
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class WeatherConditionTests(APITestCase):

    
    def test_invalid_long_input(self):
        data={"Town":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
        client=APIClient()
        response = client.post("/weatherCondition/api/",data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_invalid_short_input(self):
        data={"Town":"shoe"}
        client=APIClient()
        response = client.post("/weatherCondition/api/",data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_input(self):
        data={"Town":"London"}
        client=APIClient()
        response = client.post("/weatherCondition/api/",data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_method(self):
        client=APIClient()
        response=client.get("/weatherCondition/api/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
