from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class AuthenticationTests(APITestCase):

    def test_wrong_password(self):
        self.data = {
            "context": {
                "data": {
                    "username": "e632hdk",
                    "name": "hasan",
                    "surname": "ali kurt",
                    "password": "123456",
                    "password2": "1234567",
                    "mail": "bela632@hotmail.com"

                }
            },
        }
        client = APIClient()
        response = client.post("/register", self.data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_existing_username(self):
        self.data = {
            "context": {
                "data": {
                    "username": "e97hdk",
                    "name": "ali",
                    "surname": "Kuşçu",
                    "password": "1234567",
                    "password2": "1234567",
                    "mail": "bela99@hotmail.com"

                }
            }
        }

        self.client.post("/register", self.data, format='json')
        response = self.client.post("/register", self.data, format='json')
        self.assertEqual(response.status_code, 409)

    def test_existing_mail(self):
        self.data2 = {
            "context": {
                "data": {
                    "username": "e99hdk",
                    "name": "badu",
                    "surname": "dudu",
                    "password": "1234567",
                    "password2": "1234567",
                    "mail": "bela991@hotmail.com"

                }
            }
        }
        self.data = {
            "context": {
                "data": {
                    "username": "e97hdk",
                    "name": "ali",
                    "surname": "Kuşçu",
                    "password": "1234567",
                    "password2": "1234567",
                    "mail": "bela991@hotmail.com"

                }
            }
        }
        self.client.post("/register", self.data, format='json')
        response = self.client.post("/register", self.data2, format='json')
        self.assertEqual(response.status_code, 409)
