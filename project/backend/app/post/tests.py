from django.test import TestCase
from register.models import User, InterestLevel  # will be changed after custom User is implemented
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from post.models import Badge, BadgeOfferedByEventPost, EquipmentPost, SkillLevel, Sport ,EventPost, Application
from register.models import InterestLevel
import json
from datetime import datetime

class PostTests(APITestCase):
# Create your tests here.
    def test_create_event_post_post(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=24,sport_name="Handball",is_custom=False)
        Badge.objects.create(id=5,name="surprised",description="You are a friendly player",pathToBadgeImage="....com")
        SkillLevel.objects.create(id=1,level_name="beginner")
        data={"image":"","json":json.dumps({
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally is creating an event post",
            "type": "Create",
            "actor": {
                "type": "Person",
                "name": "Sally",
                "surname": "Sparrow" ,"username":"crazy_girl","Id":321
            },
            "object": {
                "type": "Event_Post",
                "owner_id": 321,
                "post_name": "abc hali saha",
                "sport_category": "Handball",
                "longitude":20.444,
                "latitude":18.555,
                "description": "adadasdasdad",
                "pathToEventImage": None,
                "date_time": "2021-02-10 10:30",
                "participant_limit": 14,
                "spectator_limit": None,
                "rule": "asd",
                "equipment_requirement": None,      
                "location_requirement": "asd",
                "contact_info": "054155555",
                "skill_requirement": "beginner",
                "repeating_frequency": 5,
                "badges": [ {"id":5,"name":"surprised","description":"You are a friendly player","pathToBadgeImage":"....com"}]
            
            }
            })
        }
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/post/create_event_post/",data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_event_post_get(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=1,sport_name="Football",is_custom=False)
        Badge.objects.create(id=1,name="friendly",description="You are a friendly player",pathToBadgeImage=None)
        SkillLevel.objects.create(id=1,level_name="beginner")
        Sport.objects.create(id=2,sport_name="Volleyball",is_custom=False)
        Badge.objects.create(id=2,name="bad",description="You are a bad player",pathToBadgeImage=None)
        SkillLevel.objects.create(id=2,level_name="expert")

        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response=client.get("/post/create_event_post/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_create_equipment_post_post(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        data={"image":"","json":json.dumps({
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally is creating an equipment post",
            "type": "Create",
            "actor": {
                "type": "Person",
                "Id":321,
                "name": "Sally",
                "surname": "Sparrow",
                "username":"crazy_girl"
            },
            "object": {
                "type": "EquipmetPost",
                "owner_id": 321,
                "post_name": "adidas bileklik",
                "sport_category": "Tennis",
                "longitude":20.444,
                "latitude":18.555,
                "description": "adadasdasdad",
                 "pathToEquipmentPostImage": None,
                "link": "https://www.adidas.com.tr/tr",
            }
            })
            }
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/post/create_equipment_post/",data,format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_equipment_post_get(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response=client.get("/post/create_equipment_post/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_delete_equipment_post(self):
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=13,sport_name="Basketball",is_custom=False)
        s=Sport.objects.get(sport_name='Basketball')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        EquipmentPost.objects.create(id=12345,post_name="adidas bileklik", owner=u,sport_category=s,created_date=dt,\
            description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                longitude=20.444,
                latitude=18.555,link='...com',active=True,pathToEquipmentPostImage="...com")

        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally deleted an equipment post",
            "type": "Delete",
            "actor": {
                "type": "Person",
                "Id":12345,
                "name": "Sally",
                "surname": "Sparrow",
                "username":"crazy_girl"
            },
            "object": {
            "type":"EquipmentPost",
            "post_id": 12345
            },
            "origin": {
                "type": "Collection",
                "name": "Sally's Event posts"
            }
            }
        
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.delete("/post/delete_equipment_post/",data,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_event_post(self):
        User.objects.create(Id=12345, first_name="Sally", last_name="Sparrow", username="crazy_girl", password="123",
                            email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=13, sport_name="Basketball", is_custom=False)
        s = Sport.objects.get(sport_name='Basketball')
        date_string = "2021-12-12 10:10"
        dt = datetime.fromisoformat(date_string)
        date_string2 = "2021-12-12 20:20"
        dt2 = datetime.fromisoformat(date_string2)
        myskill = SkillLevel.objects.create(id=1,level_name="beginner")
        EventPost.objects.create(id=12345, post_name="hali saha", owner=u, sport_category=s, created_date=dt, \
                                     description="We need 5 player to hali saha on Friday", \
                                     longitude=20.444, latitude=18.555, date_time=dt2, participant_limit=5, spectator_limit=0, rule="", \
                                 equipment_requirement="", status="upcoming", capacity="open to application", location_requirement="", \
                                 contact_info="", skill_requirement=myskill)

        data = {
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally deleted an event post",
            "type": "Delete",
            "actor": {
                "type": "Person",
                "Id": 12345,
                "name": "Sally",
                "surname": "Sparrow",
                "username": "crazy_girl"
            },
            "object": {
                "type": "EquipmentPost",
                "post_id": 12345
            },
            "origin": {
                "type": "Collection",
                "name": "Sally's Event posts"
            }
        }

        client = APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.delete("/post/delete_event_post/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)




    def test_change_equipment_post_invalid_info(self):
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=15,sport_name="Running",is_custom=False)
        s=Sport.objects.get(sport_name='Running')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        EquipmentPost.objects.create(id=12345,post_name="adidas bileklik", owner=u,sport_category=s,created_date=dt,\
            description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                longitude=20.444,
                latitude=18.555,link='...com',active=True,pathToEquipmentPostImage="...com")

        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally updated an equipment post",
            "type": "Update",
            "actor": {
                "type": "Person",
                "Id":12345,
                "name": "Sally",
                "surname": "Sparrow",
                "username":"crazy_girl"
            },
            "object": {
            "type":"EquipmentPost",
            "post_id": 12345
            },
            "modifications": {
                "post_name":"adidas harika bileklik<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<",
                "sport_category":"Football", 
                "description":"blabla", 
                "latitude":32.666, 
                "longitude":12.5678,
                "link":"https://www.adidas.com.tr/tr",
                "pathToEquipmentPostImage":None
                }
            }
        
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.patch("/post/change_equipment_post/",data,format='json')
        self.assertEqual(response.status_code, 422)
    
    def test_change_equipment_post_valid_info(self):
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=17,sport_name="Jogging",is_custom=False)
        s=Sport.objects.get(sport_name='Jogging')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        EquipmentPost.objects.create(id=12345,post_name="adidas bileklik", owner=u,sport_category=s,created_date=dt,\
            description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                longitude=20.444,
                latitude=18.555,link='...com',active=True,pathToEquipmentPostImage="...com")

        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally updated an equipment post",
            "type": "Update",
            "actor": {
                "type": "Person",
                "Id":12345,
                "name": "Sally",
                "surname": "Sparrow",
                "username":"crazy_girl"
            },
            "object": {
            "type":"EquipmentPost",
            "post_id": 12345
            },
            "modifications": {
                "post_name":"adidas harika bileklik",
                "sport_category":"Football", 
                "description":"blabla", 
                "link":"https://www.adidas.com.tr/tr",
                "pathToEquipmentPostImage":None
                }
            }
        
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.patch("/post/change_equipment_post/",data,format='json')
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_change_event_post_valid_info(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=10,sport_name="Swimming",is_custom=False)
        s=Sport.objects.get(sport_name='Swimming')
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
        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally is updating event post",
            "type": "Update",
            "actor": {
                "type": "Person",
                "name": "Sally",
                "surname": "Sparrow" ,"username":"crazy_girl","Id":321
            },
            "object": {
                "type":"EventPost",
                "post_id":1
            },
            "modifications": {
                "post_name":"Ali'nin basket maçı",
                 "description":"blabla", 
                 "location":None, 
                 "participant_limit":10, 
                 "spectator_limit":30,
                  "equipment_requirement": "Racket",
                   "date_time": "2021-12-13 10:10", 
                     "location_requirement": "In 250 m radius",
                     "rule": "Don't shout", 
                     "skill_requirement": "medium", 
                     "contact_info": "05555555555",
                      "badges":[{"id":1,"name":"awesome","description":"You are an awesome player","pathToBadgeImage":"....com"}], 
                      "image":None
            }
            }

        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.patch("/post/change_event_post/",data,format='json')
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_apply_to_event_valid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
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
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)

        ## data
        data = {
                "actor": {
                    "type": "Person",
                    "name": "Sally",
                    "surname": "Sparrow",
                    "username": "crazy_girl",
                    "Id": 12345
                },
                "event_id": 10
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/post/apply_to_event/",data,format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)


    def test_apply_to_event_invalid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
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
                                 capacity="full", \
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=20, current_spectator=0)

        ## data
        data = {
                "actor": {
                    "type": "Person",
                    "name": "Sally",
                    "surname": "Sparrow",
                    "username": "crazy_girl",
                    "Id": 12345
                },
                "event_id": 10
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/post/apply_to_event/",data,format='json')
        print(response.data)
        self.assertEqual(response.status_code, 400)



    def test_spectate_to_event_valid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345, first_name="Sally", last_name="Sparrow", username="crazy_girl", password="123",
                            email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
        date_string = "2021-12-12 10:10"
        dt = datetime.fromisoformat(date_string)

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
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)

        ## data
        data = {
            "actor": {
                "type": "Person",
                "name": "Sally",
                "surname": "Sparrow",
                "username": "crazy_girl",
                "Id": 12345
            },
            "event_id": 10
        }

        client = APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/post/spectate_to_event/", data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)

    def test_spectate_to_event_invalid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345, first_name="Sally", last_name="Sparrow", username="crazy_girl", password="123",
                            email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
        date_string = "2021-12-12 10:10"
        dt = datetime.fromisoformat(date_string)

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
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=30)

        ## data
        data = {
            "actor": {
                "type": "Person",
                "name": "Sally",
                "surname": "Sparrow",
                "username": "crazy_girl",
                "Id": 12345
            },
            "event_id": 10
        }

        client = APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/post/spectate_to_event/", data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 400)



###
    def test_accept_application_valid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
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
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)

        Application.objects.filter(id=5, event_post_id=10, user_id=12345, status="waiting", applicant_type="player")

        ## data
        data = {
            "event_Id": 10,
            "applicant_Id": 12345
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/post/accept_application/",data,format='json')
        print(response.data)
        self.assertEqual(response.status_code, 200)

###
    def test_accept_application_invalid(self):
        ## Creating user and adding an interest to her
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
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
                                 capacity="cancelled", \
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)

        Application.objects.filter(id=5, event_post_id=10, user_id=12345, status="waiting", applicant_type="player")

        ## data
        data = {
            "event_Id": 10,
            "applicant_Id": 12345
        }


        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/post/accept_application/",data,format='json')
        print(response.data)
        self.assertEqual(response.status_code, 400)
##*****



    def test_get_spectators_invalid(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()

        ## there is no spectator in this event so it gives an error
        client = APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.get("/post/get_spectators/?eventId=3", format='json')
        self.assertEqual(response.status_code, 404)

    def test_get_spectators_valid(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        SkillLevel.objects.create(id=1, level_name="beginner")
        skill = SkillLevel.objects.get(level_name='beginner')

        event = EventPost.objects.create(id=3, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="full", \
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=20, current_spectator=0)



        ## there is no spectator in this event so it gives an error
        Application.objects.create(user_id=321, event_post=event, status="accepted", applicant_type="spectator")



        client = APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.get("/post/get_spectators/?eventId=3", format='json')
        self.assertEqual(response.status_code, 200)





    def test_change_event_post_invalid_info(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
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
        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally is updating event post",
            "type": "Update",
            "actor": {
                "type": "Person",
                "name": "Sally",
                "surname": "Sparrow" ,"username":"crazy_girl","Id":321
            },
            "object": {
                "type":"EventPost",
                "post_id":1
            },
            "modifications": {
                "post_name":"Ali'nin basket maçı<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<",
                 "description":"blabla", 
                 "location":None, 
                 "participant_limit":10, 
                 "spectator_limit":30,
                  "equipment_requirement": "Racket",
                   "date_time": "2021-12-13 10:10", 
                     "location_requirement": "In 250 m radius",
                     "rule": "Don't shout", 
                     "skill_requirement": "medium", 
                     "contact_info": "05555555555",
                      "badges":[{"id":1,"name":"awesome","description":"You are an awesome player","pathToBadgeImage":"....com"}], 
                      "image":None
            }
            }

        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.patch("/post/change_event_post/",data,format='json')
        self.assertEqual(response.status_code, 422)

    def test_get_event_post_details(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=10,sport_name="Swimming",is_custom=False)
        s=Sport.objects.get(sport_name='Swimming')
        Badge.objects.create(id=1,name="awesome",description="You are an awesome player",pathToBadgeImage="....com")
        Badge.objects.create(id=5,name="surprised",description="You are a surprised player",pathToBadgeImage="....com")
        b=Badge.objects.get(id=1)
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
        e=EventPost.objects.get(id=1)
        BadgeOfferedByEventPost.objects.create(id=1,post=e,badge=b)
        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally read an event post",
            "type": "View",
            "actor": {
                "type": "Person",
                "name": "Sally",
            "surname": "Sparrow" ,"username":"crazy_girl","Id":321
            },
            "object": {
                "type": "EventPost",
                "post_id":1
            }
            }
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/post/get_event_post_details/",data,format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)

    def test_get_equipment_post_details(self):
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=17,sport_name="Jogging",is_custom=False)
        s=Sport.objects.get(sport_name='Jogging')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        EquipmentPost.objects.create(id=1,post_name="adidas bileklik", owner=u,sport_category=s,\
            created_date=dt,description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                longitude=20.444,
                latitude=18.555,link='...com',active=True,pathToEquipmentPostImage="...com")

        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally read an equipment post",
            "type": "View",
            "actor": {
                "type": "Person",
                "name": "Sally",
            "surname": "Sparrow" ,"username":"crazy_girl","Id":12345
            },
            "object": {
                "type": "EquipmentPost",
                "post_id":1
            }
            }
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/post/get_equipment_post_details/",data,format='json')
        print(response.data)
        self.assertEqual(response.status_code, 201)


    def test_get_waiting_applications_valid(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        SkillLevel.objects.create(id=1, level_name="beginner")
        skill = SkillLevel.objects.get(level_name='beginner')

        event = EventPost.objects.create(id=3, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="full", \
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)



        ## there is no spectator in this event so it gives an error
        Application.objects.create(user_id=321, event_post=event, status="waiting", applicant_type="player")



        client = APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.get("/post/get_waiting_applications/?eventId=3", format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_waiting_applications_invalid(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        SkillLevel.objects.create(id=1, level_name="beginner")
        skill = SkillLevel.objects.get(level_name='beginner')

        event = EventPost.objects.create(id=3, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="full", \
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)



        ## there is no spectator in this event so it gives an error
        #Application.objects.create(user_id=321, event_post=event, status="waiting", applicant_type="player")
        ## now there is no application for this event so empty list will be returned and status will be 404


        client = APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.get("/post/get_waiting_applications/?eventId=3", format='json')
        self.assertEqual(response.status_code, 404)


##
    def test_get_accepted_applications_valid(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        SkillLevel.objects.create(id=1, level_name="beginner")
        skill = SkillLevel.objects.get(level_name='beginner')

        event = EventPost.objects.create(id=3, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="full", \
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)



        ## there is no spectator in this event so it gives an error
        Application.objects.create(user_id=321, event_post=event, status="accepted", applicant_type="player")



        client = APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.get("/post/get_accepted_applications/?eventId=3", format='json')
        self.assertEqual(response.status_code, 200)
##

    def test_get_rejected_applications_valid(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        SkillLevel.objects.create(id=1, level_name="beginner")
        skill = SkillLevel.objects.get(level_name='beginner')

        event = EventPost.objects.create(id=3, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="full", \
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)



        ## there is no spectator in this event so it gives an error
        Application.objects.create(user_id=321, event_post=event, status="rejected", applicant_type="player")



        client = APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.get("/post/get_rejected_applications/?eventId=3", format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_inadequate_applications_valid(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=34, sport_name="Football", is_custom=False)
        s = Sport.objects.get(sport_name='Football')
        date_string = "2021-12-12 10:10"
        dt=datetime.fromisoformat(date_string)
        SkillLevel.objects.create(id=1, level_name="beginner")
        skill = SkillLevel.objects.get(level_name='beginner')

        event = EventPost.objects.create(id=3, post_name="Aksama hali saha", owner=u, sport_category=s, created_date=dt,
                                 description="blabla", \
                                 longitude=20.444,
                                 latitude=18.555, date_time=dt, participant_limit=20, \
                                 spectator_limit=30, rule="don't shout", equipment_requirement=None, status="upcoming",
                                 capacity="full", \
                                 location_requirement=None, contact_info="0555555555555", pathToEventImage=None,
                                 skill_requirement=skill, current_player=0, current_spectator=0)



        ## there is no spectator in this event so it gives an error
        Application.objects.create(user_id=321, event_post=event, status="inadeq", applicant_type="player")



        client = APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.get("/post/get_inadequate_applications/?eventId=3", format='json')
        self.assertEqual(response.status_code, 200)