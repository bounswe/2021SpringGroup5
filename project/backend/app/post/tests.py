from django.test import TestCase
from register.models import User  # will be changed after custom User is implemented
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from post.models import Badge, EquipmentPost, SkillLevel, Sport ,EventPost
import json
from datetime import datetime

class PostTests(APITestCase):
# Create your tests here.
    def test_create_event_post_post(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=24,sport_name="Handball")
        Badge.objects.create(id=5,name="surprised",description="You are a friendly player",pathToBadgeImage="....com")
        SkillLevel.objects.create(id=1,level_name="beginner")
        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally is creating an event post",
            "type": "Create",
            "actor": {
                "type": "Person",
                "name": "Sally",
                "surname": "Sparrow" ,"username":"crazy_girl","id":321
            },
            "object": {
                "type": "Event_Post",
                "owner_id": 321,
                "post_name": "abc hali saha",
                "sport_category": "Handball",
                "country":'Turkey',
                "city":'İstanbul',
                "neighborhood":'Kadıköy',
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
                "repeating_frequency": "5",
                "badges": [ {"id":5,"name":"surprised","description":"You are a friendly player","pathToBadgeImage":"....com"}]
            
            }
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
        Sport.objects.create(id=1,sport_name="Football")
        Badge.objects.create(id=1,name="friendly",description="You are a friendly player",pathToBadgeImage=None)
        SkillLevel.objects.create(id=1,level_name="beginner")
        Sport.objects.create(id=2,sport_name="Volleyball")
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
        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally is creating an equipment post",
            "type": "Create",
            "actor": {
                "type": "Person",
                "id":321,
                "name": "Sally",
                "surname": "Sparrow",
                "username":"crazy_girl"
            },
            "object": {
                "type": "EquipmetPost",
                "owner_id": 321,
                "post_name": "adidas bileklik",
                "sport_category": "Tennis",
                "country":'Turkey',
                "city":None,
                "neighborhood":None,
                "description": "adadasdasdad",
            "pathToEquipmentPostImage": None,
                "link": "https://www.adidas.com.tr/tr",
            }
            }
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.post("/post/create_equipment_post/",data,format='json')
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
        Sport.objects.create(id=13,sport_name="Basketball")
        s=Sport.objects.get(sport_name='Basketball')
        EquipmentPost.objects.create(id=12345,post_name="adidas bileklik", owner=u,sport_category=s,\
            description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                country='Turkey',city='Istanbul',neighborhood='Kadıkoy',link='...com',active=True,pathToEquipmentPostImage="...com")

        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally deleted an equipment post",
            "type": "Delete",
            "actor": {
                "type": "Person",
                "id":12345,
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

    def test_change_equipment_post_invalid_info(self):
        User.objects.create(Id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=15,sport_name="Running")
        s=Sport.objects.get(sport_name='Running')
        EquipmentPost.objects.create(id=12345,post_name="adidas bileklik", owner=u,sport_category=s,\
            description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                country='Turkey',city='Istanbul',neighborhood='Kadıkoy',link='...com',active=True,pathToEquipmentPostImage="...com")

        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally updated an equipment post",
            "type": "Update",
            "actor": {
                "type": "Person",
                "id":12345,
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
                "neighborhood":None, 
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
        Sport.objects.create(id=17,sport_name="Jogging")
        s=Sport.objects.get(sport_name='Jogging')
        EquipmentPost.objects.create(id=12345,post_name="adidas bileklik", owner=u,sport_category=s,\
            description="There is a big discount at this store for adidas bileklik. Don't miss it!",\
                country='Turkey',city='Istanbul',neighborhood='Kadıkoy',link='...com',active=True,pathToEquipmentPostImage="...com")

        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally updated an equipment post",
            "type": "Update",
            "actor": {
                "type": "Person",
                "id":12345,
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
                "neighborhood":None, 
                "link":"https://www.adidas.com.tr/tr",
                "pathToEquipmentPostImage":None
                }
            }
        
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.patch("/post/change_equipment_post/",data,format='json')
        self.assertEqual(response.status_code, 200)

    def test_change_event_post_valid_info(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=10,sport_name="Swimming")
        s=Sport.objects.get(sport_name='Swimming')
        Badge.objects.create(id=1,name="awesome",description="You are an awesome player",pathToBadgeImage="....com")
        Badge.objects.create(id=5,name="surprised",description="You are a surprised player",pathToBadgeImage="....com")
        SkillLevel.objects.create(id=1,level_name="beginner")
        SkillLevel.objects.create(id=2,level_name="medium")
        skill=SkillLevel.objects.get(level_name='beginner')
        date_string = "2021-12-12 10:10:10"
        dt=datetime.fromisoformat(date_string)
        EventPost.objects.create(id=1, post_name="Ali'nin maçı", owner=u,sport_category=s,description="blabla",\
            country="Turkey", city="Istanbul", neighborhood=None,date_time=dt, participant_limit=20,\
                spectator_limit=30,rule="don't shout",equipment_requirement=None,status="upcoming",capacity="open to applications",\
                    location_requirement=None,contact_info="0555555555555",repeating_frequency=1,pathToEventImage=None,skill_requirement=skill)
        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally is updating event post",
            "type": "Update",
            "actor": {
                "type": "Person",
                "name": "Sally",
                "surname": "Sparrow" ,"username":"crazy_girl","id":321
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
                   "date_time": "2021-12-13 10:10:10", 
                     "location_requirement": "In 250 m radius",
                     "rule": "Don't shout", 
                     "skill_requirement": "medium", 
                     "contact_info": "05555555555",
                      "repeating_frequency": 1, 
                      "badges":["awesome"], 
                      "image":None
            }
            }

        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.patch("/post/change_event_post/",data,format='json')
        self.assertEqual(response.status_code, 200)


    def test_change_event_post_invalid_info(self):
        User.objects.create(Id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=19,sport_name="Cycling")
        s=Sport.objects.get(sport_name='Cycling')
        Badge.objects.create(id=1,name="awesome",description="You are an awesome player",pathToBadgeImage="....com")
        Badge.objects.create(id=5,name="surprised",description="You are a surprised player",pathToBadgeImage="....com")
        SkillLevel.objects.create(id=1,level_name="beginner")
        SkillLevel.objects.create(id=2,level_name="medium")
        skill=SkillLevel.objects.get(level_name='beginner')
        date_string = "2021-12-12 10:10:10"
        dt=datetime.fromisoformat(date_string)
        EventPost.objects.create(id=1, post_name="Ali'nin maçı", owner=u,sport_category=s,description="blabla",\
            country="Turkey", city="Istanbul", neighborhood=None,date_time=dt, participant_limit=20,\
                spectator_limit=30,rule="don't shout",equipment_requirement=None,status="upcoming",capacity="open to applications",\
                    location_requirement=None,contact_info="0555555555555",repeating_frequency=1,pathToEventImage=None,skill_requirement=skill)
        data={
            "@context": "https://www.w3.org/ns/activitystreams",
            "summary": "Sally is updating event post",
            "type": "Update",
            "actor": {
                "type": "Person",
                "name": "Sally",
                "surname": "Sparrow" ,"username":"crazy_girl","id":321
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
                   "date_time": "2021-12-13 10:10:10", 
                     "location_requirement": "In 250 m radius",
                     "rule": "Don't shout", 
                     "skill_requirement": "medium", 
                     "contact_info": "05555555555",
                      "repeating_frequency": 1, 
                      "badges":["awesome"], 
                      "image":None
            }
            }

        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.patch("/post/change_event_post/",data,format='json')
        self.assertEqual(response.status_code, 422)

