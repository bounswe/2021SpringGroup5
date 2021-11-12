from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class AuthenticationTests(APITestCase):

    def test_wrong_password(self):
        self.data = {
            "actor": {
                "username": "e63hdk",
                "name": "hasan",
                "surname": "ali kurt",
                "password1": "123456",
                "password2": "1234567",
                "email": "bela55@hotmail.com"


            },
            "items": [
                {
                    "name": "football",
                    "level": "advanced"
                },
                {
                    "name": "volleyball",
                    "level": "beginner"
                }

            ]

        }
        client = APIClient()
        response = client.post("/register", self.data, format='json')
        self.assertEqual(response.status_code, 401)

    def test_existing_username(self):
        self.data = {
            "actor": {
                "username": "e632hdk",
                "name": "hasan",
                "surname": "ali kurt",
                "password1": "1234567",
                "password2": "1234567",
                "email": "bela632@hotmail.com"

            },
            "items": [
                {
                    "name": "football",
                    "level": "advanced"
                },
                {
                    "name": "volleyball",
                    "level": "beginner"
                }

            ]

        }

        self.client.post("/register", self.data, format='json')
        response = self.client.post("/register", self.data, format='json')
        self.assertEqual(response.status_code, 409)

    def test_existing_mail(self):
        self.data2 = {
            "actor": {
                "username": "e632hdk",
                "name": "hasan",
                "surname": "ali kurt",
                "password1": "1234567",
                "password2": "1234567",
                "email": "bela632@hotmail.com"

            },
            "items": [
                {
                    "name": "football",
                    "level": "advanced"
                },
                {
                    "name": "volleyball",
                    "level": "beginner"
                }

            ]

        }
        self.data = {
            "actor": {
                "username": "e571hdk",
                "name": "hasan",
                "surname": "ali kurt",
                "password1": "1234567",
                "password2": "1234567",
                "email": "bela632@hotmail.com"

            },
            "items": [
                {
                    "name": "football",
                    "level": "advanced"
                },
                {
                    "name": "volleyball",
                    "level": "beginner"
                }

            ]

        }
        self.client.post("/register", self.data, format='json')
        response = self.client.post("/register", self.data2, format='json')
        self.assertEqual(response.status_code, 409)

    def test_register(self):
        self.data = {
            "actor": {
                "username": "e1453hdk",
                "name": "hasan",
                "surname": "ali kurt",
                "password1": "hisimım",
                "password2": "hisimım",
                "email": "bela1453@hotmail.com"

            },
            "items": [
                {
                    "name": "football",
                    "level": "advanced"
                },
                {
                    "name": "volleyball",
                    "level": "beginner"
                }

            ]

        }
        client = APIClient()
        response = client.post("/register", self.data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        self.data = {
            "actor": {
                "username": "e751hdk",
                "name": "SERHAT",
                "surname": "BAYRAKTAR",
                "password1": "hisimım",
                "password2": "hisimım",
                "email": "yesiltepelibela109@hotmail.com"

            },
            "items": [
                {
                    "name": "football",
                    "level": "advanced"
                },
                {
                    "name": "volleyball",
                    "level": "beginner"
                }

            ]

        }
        self.data2 = {
            "actor": {
                "username": "e751hdk",
                "surname": "BAYRAKTAR",
                "password": "hisimım",

            },
            "items": [
                {
                    "name": "football",
                    "level": "advanced"
                },
                {
                    "name": "volleyball",
                    "level": "beginner"
                }

            ]

        }

        self.client.post("/register", self.data, format='json')
        response = self.client.post("/login", self.data2, format='json')
        self.assertEqual(response.status_code, 200)