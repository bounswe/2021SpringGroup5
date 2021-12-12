from django.test import TestCase
from register.models import User  # will be changed after custom User is implemented
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from post.models import Badge, BadgeOfferedByEventPost, EquipmentPost, SkillLevel, Sport ,EventPost
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
        data={
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
        data={
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
                "link": "https://www.adidas.com.tr/tr",
            }
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
                latitude=18.555,link='...com',active=True)

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
                latitude=18.555,link='...com',active=True)

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
                latitude=18.555,link='...com',active=True)

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
                    location_requirement=None,contact_info="0555555555555",skill_requirement=skill)
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
                    location_requirement=None,contact_info="0555555555555",skill_requirement=skill)
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
                    location_requirement=None,contact_info="0555555555555",skill_requirement=skill)
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
                latitude=18.555,link='...com',active=True)

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