from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from post.models import Sport,Badge,EventPost,SkillLevel
from .models import User,Follow
from datetime import datetime
class AuthenticationTests(APITestCase):

    def test_wrong_password(self):
        Sport.objects.create(id=1,sport_name="football", is_custom=False)
        Sport.objects.create(id=2,sport_name="volleyball", is_custom=False)
        self.data = {
            "actor": {
                "username": "e6333hdk",
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
        Sport.objects.create(id=1,sport_name="football", is_custom=False)
        Sport.objects.create(id=2,sport_name="volleyball", is_custom=False)
        self.data = {
            "actor": {
                "username": "e6323hdk",
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
        Sport.objects.create(id=1,sport_name="football", is_custom=False)
        Sport.objects.create(id=2,sport_name="volleyball", is_custom=False)
        self.data2 = {
            "actor": {
                "username": "e6321hdk",
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
                "username": "e5711hdk",
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
        Sport.objects.create(id=1,sport_name="football", is_custom=False)
        Sport.objects.create(id=2,sport_name="volleyball", is_custom=False)
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
        Sport.objects.create(id=1,sport_name="football", is_custom=False)
        Sport.objects.create(id=2,sport_name="volleyball", is_custom=False)
        self.data = {
            "actor": {
                "username": "e75112hdk",
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
                "username": "e75112hdk",
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

    def test_home_page(self):
        User.objects.create(Id=1,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u1 = User.objects.get(username='crazy_girl')
        u1.set_password('123')
        u1.save()

        User.objects.create(Id=2,first_name="Cindy",last_name="Sparrow",username="cindy_girl",password="123",email="...com")
        u = User.objects.get(username='cindy_girl')
        u.set_password('123')
        u.save()

        Follow.objects.create(Id=1,follower=u1,following=u)

        Sport.objects.create(id=19,sport_name="Cycling",is_custom=False)
        s=Sport.objects.get(sport_name='Cycling')
        Badge.objects.create(id=1,name="awesome",description="You are an awesome player",pathToBadgeImage="....com")
        Badge.objects.create(id=5,name="surprised",description="You are a surprised player",pathToBadgeImage="....com")
        SkillLevel.objects.create(id=1,level_name="beginner")
        SkillLevel.objects.create(id=2,level_name="medium")
        skill=SkillLevel.objects.get(level_name='beginner')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        EventPost.objects.create(id=1, post_name="Ali'nin maçı", owner=u,sport_category=s,created_date=dt,description="blabla",\
            longitude=20.444,
                latitude=18.555,date_time=dt, participant_limit=20,\
                spectator_limit=30,rule="don't shout",equipment_requirement=None,status="upcoming",capacity="open to applications",\
                    location_requirement=None,contact_info="0555555555555",pathToEventImage=None,skill_requirement=skill)

        client = APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.get("home/", format='json')
        self.assertEqual(response.status_code, 200)