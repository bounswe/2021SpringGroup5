from django.test import TestCase
from register.models import User, InterestLevel
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from post.models import Badge, BadgeOfferedByEventPost, EquipmentPost, SkillLevel, Sport ,EventPost, Application
import json
from datetime import datetime

class SearchTests(APITestCase):

######## Search event post test cases
    def test_search_event_by_name_valid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example event post
        EventPost.objects.create(id=10, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)


        EventPost.objects.create(id=11, post_name="Havuz partisi", owner=u, sport_category=s2, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)





        ## data
        data = {
            "status": "upcoming",
            "search_query": "saha",                     ## query search keyword 'saha' in sport names and event names
            "sort_func": {
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": None,
                "sportType": "",
                "date": None,
                "capacity": "open to applications"
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_event/",data,format='json')
        self.assertEqual(response.status_code, 200)
##
    def test_search_event_by_name_invalid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example event post
        EventPost.objects.create(id=10, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)


        EventPost.objects.create(id=11, post_name="Havuz partisi", owner=u, sport_category=s2, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)





        ## data
        data = {
            "status": "upcoming",
            "search_query": "inv query",                     ## query search keyword 'inv query' in sport names and event names
            "sort_func": {                                   ## it does not match anything
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": None,
                "sportType": "",
                "date": None,
                "capacity": "open to applications"
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_event/",data,format='json')
        self.assertEqual(response.status_code, 404)
##
    def test_search_event_by_date_valid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        date_string2 = "2024-12-12 10:10"
        dt2=datetime.fromisoformat(date_string2)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example event post
        EventPost.objects.create(id=10, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)


        EventPost.objects.create(id=11, post_name="Havuz partisi", owner=u, sport_category=s2, created_date=dt2,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt2, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)


        ### first event is in the search date interval
        ## firsst event in 2021, second event 2024

        ## data
        data = {
            "status": "upcoming",
            "search_query": "",
            "sort_func": {
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": None,
                "sportType": "",
                "date": {
                    "startDate": "15/10/2020:20",           ## first event is in the interval, but second event is not
                    "endDate": "15/10/2022:20"
                },
                "capacity": "open to applications"
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_event/",data,format='json')
        self.assertEqual(response.status_code, 200)
##
    def test_search_event_by_date_invalid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        date_string2 = "2024-12-12 10:10"
        dt2=datetime.fromisoformat(date_string2)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example event post
        EventPost.objects.create(id=10, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)


        EventPost.objects.create(id=11, post_name="Havuz partisi", owner=u, sport_category=s2, created_date=dt2,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt2, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)


        ## data
        data = {
            "status": "upcoming",
            "search_query": "",
            "sort_func": {
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": None,
                "sportType": "",
                "date": {
                    "startDate": "15/10/2014:20",               ### both events are not in the search interval
                    "endDate": "15/10/2015:20"                  ## search function does not find a match
                },
                "capacity": "open to applications"
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_event/",data,format='json')
        self.assertEqual(response.status_code, 404)
##
    def test_search_event_by_location_valid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        date_string2 = "2024-12-12 10:10"
        dt2=datetime.fromisoformat(date_string2)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example event post
        EventPost.objects.create(id=10, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=16,
                                 latitude=15.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)


        EventPost.objects.create(id=11, post_name="Havuz partisi", owner=u, sport_category=s2, created_date=dt2,
                                 description="blabla", \
                                 longitude=25.444,
                                 latitude=25.555, date_time=dt2, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)


        ## data
        data = {
            "status": "upcoming",
            "search_query": "",
            "sort_func": {
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": {
                    "lat": 15.00,                   ## first event is in the radius
                    "lng": 16.00,
                    "radius": 3
                },
                "sportType": "",
                "date": None,
                "capacity": "open to applications"
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_event/",data,format='json')
        self.assertEqual(response.status_code, 200)
##
    def test_search_event_by_location_invalid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        date_string2 = "2024-12-12 10:10"
        dt2=datetime.fromisoformat(date_string2)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example event post
        EventPost.objects.create(id=10, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=16,
                                 latitude=15.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)


        EventPost.objects.create(id=11, post_name="Havuz partisi", owner=u, sport_category=s2, created_date=dt2,
                                 description="blabla", \
                                 longitude=25.444,
                                 latitude=25.555, date_time=dt2, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="open to applications", \
                                 location_requirement=None, contact_info="0555555555555", repeating_frequency=3, pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)

        ### both events are too far from the location we want



        ## data
        data = {
            "status": "upcoming",
            "search_query": "",
            "sort_func": {
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": {
                    "lat": 200.00,                      ## no event is in the radius
                    "lng": 250.00,
                    "radius": 5
                },
                "sportType": "",
                "date": None,
                "capacity": "open to applications"
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_event/",data,format='json')
        self.assertEqual(response.status_code, 404)


######## Search equipment posts test cases
    def test_search_equipment_by_name_valid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example equipment post
        EquipmentPost.objects.create(id=124,post_name="adidas bileklik", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=20.444,
                                        latitude=18.555,link='...com',active=True,pathToEquipmentPostImage="...com")


        EquipmentPost.objects.create(id=125,post_name="futbol topu", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=20.444,
                                        latitude=18.555,link='...com',active=True,pathToEquipmentPostImage="...com")

        ## data
        data = {
            "status": "upcoming",
            "search_query": "bileklik",                     ## query search keyword 'bileklik' in sport names and equipment post names
            "sort_func": {                                  ## there is one event named 'adidas bileklik' so search function must find a post
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": None,
                "sportType": "",
                "created_date": None
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_equipment/",data,format='json')
        self.assertEqual(response.status_code, 200)
##
    def test_search_equipment_by_name_invalid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example equipment post
        EquipmentPost.objects.create(id=124,post_name="adidas bileklik", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=20.444,
                                        latitude=18.555,link='...com',active=False,pathToEquipmentPostImage="...com")


        EquipmentPost.objects.create(id=125,post_name="futbol topu", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=20.444,
                                        latitude=18.555,link='...com',active=True,pathToEquipmentPostImage="...com")

        ## data
        data = {
            "status": "upcoming",
            "search_query": "bileklik",                     ## query search keyword 'bileklik' in sport names and equipment names
            "sort_func": {                                  ## this time one post does not contain 'bileklik' and the other post is not active so program does not find a post
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": None,
                "sportType": "",
                "created_date": None
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_equipment/",data,format='json')
        self.assertEqual(response.status_code, 404)
##
    def test_search_equipment_by_location_valid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example equipment post
        EquipmentPost.objects.create(id=124,post_name="adidas bileklik", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=17.444,
                                        latitude=17.555,link='...com',active=True,pathToEquipmentPostImage="...com")


        EquipmentPost.objects.create(id=125,post_name="futbol topu", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=200.444,
                                        latitude=180.555,link='...com',active=True,pathToEquipmentPostImage="...com")

        ## data
        data = {
            "status": "upcoming",
            "search_query": "",
            "sort_func": {
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": {
                    "lat": 15.000,                  ## one post is in the radius
                    "lng": 20.000,
                    "radius": 10
                },
                "sportType": "",
                "created_date": None
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_equipment/",data,format='json')
        self.assertEqual(response.status_code, 200)
##
    def test_search_equipment_by_location_invalid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example equipment post
        EquipmentPost.objects.create(id=124,post_name="adidas bileklik", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=17.444,
                                        latitude=17.555,link='...com',active=True,pathToEquipmentPostImage="...com")


        EquipmentPost.objects.create(id=125,post_name="futbol topu", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=15.444,
                                        latitude=15.555,link='...com',active=True,pathToEquipmentPostImage="...com")

        ## data
        data = {
            "status": "upcoming",
            "search_query": "",
            "sort_func": {
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": {
                    "lat": 200.000,                     ## no post is in the radius
                    "lng": 150.000,
                    "radius": 10
                },
                "sportType": "",
                "created_date": None
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_equipment/",data,format='json')
        self.assertEqual(response.status_code, 404)
##
    def test_search_equipment_by_date_valid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example equipment post
        EquipmentPost.objects.create(id=124,post_name="adidas bileklik", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=17.444,
                                        latitude=17.555,link='...com',active=True,pathToEquipmentPostImage="...com")


        EquipmentPost.objects.create(id=125,post_name="futbol topu", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=200.444,
                                        latitude=180.555,link='...com',active=True,pathToEquipmentPostImage="...com")

        ## data
        data = {
            "status": "upcoming",
            "search_query": "",
            "sort_func": {
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": None,
                "sportType": "",
                "created_date": {
                    "startDate": "10/10/2020:20",           ## both posts are in the time interval
                    "endDate": "10/10/2022:20"
                }
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_equipment/",data,format='json')
        self.assertEqual(response.status_code, 200)
##
    def test_search_equipment_by_date_invalid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football")
        s = Sport.objects.get(sport_name='Football')
        Sport.objects.create(id=35, sport_name="Swimming")
        s2 = Sport.objects.get(sport_name='Swimming')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)

        InterestLevel.objects.create(id=1, skill_level="beginner", owner_of_interest_id=12345, sport_name_id=34)


        ## Creating mock skill level and get it
        SkillLevel.objects.create(id=1, level_name="beginner")
        SkillLevel.objects.create(id=2, level_name="medium")
        skill = SkillLevel.objects.get(level_name='beginner')

        ## Creating example equipment post
        EquipmentPost.objects.create(id=124,post_name="adidas bileklik", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=17.444,
                                        latitude=17.555,link='...com',active=True,pathToEquipmentPostImage="...com")


        EquipmentPost.objects.create(id=125,post_name="futbol topu", owner=u,sport_category=s,created_date=dt,\
                                    description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                                        longitude=200.444,
                                        latitude=180.555,link='...com',active=True,pathToEquipmentPostImage="...com")


        ## data
        data = {
            "status": "upcoming",
            "search_query": "",
            "sort_func": {
                "isSortedByLocation": False
            },
            "filter_func": {
                "location": None,
                "sportType": "",
                "created_date": {
                    "startDate": "10/10/2014:20",           ## search interval contains zero match
                    "endDate": "10/10/2016:20"
                }
            }
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/search/search_equipment/",data,format='json')
        self.assertEqual(response.status_code, 404)
