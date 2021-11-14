from django.test import TestCase
from django.contrib.auth.models import User # will be changed after custom User is implemented
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from post.models import Badge, EquipmentPost, SkillLevel, Sport 
import json
class PostTests(APITestCase):
# Create your tests here.
    def test_create_event_post_post(self):
        User.objects.create(id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=4,sport_name="Handball")
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
                "name": "abc hali saha",
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
                "status": 0,
                "capacity": "open to applications",
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
        User.objects.create(id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=1,sport_name="Football")
        Badge.objects.create(id=1,name="friendly",description="You are a friendly player",pathToBadgeImage="....com")
        SkillLevel.objects.create(id=1,level_name="beginner")
        Sport.objects.create(id=2,sport_name="Volleyball")
        Badge.objects.create(id=2,name="bad",description="You are a friendly player",pathToBadgeImage="....com")
        SkillLevel.objects.create(id=2,level_name="expert")

        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response=client.get("/post/create_event_post/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_create_equipment_post_post(self):
        User.objects.create(id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=4,sport_name="Handball")
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
                "name": "adidas bileklik",
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
        User.objects.create(id=321,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response=client.get("/post/create_equipment_post/")
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_delete_equipment_post(self):
        User.objects.create(id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=4,sport_name="Handball")
        s=Sport.objects.get(sport_name='Handball')
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

    def test_change_equipment_post_info(self):
        User.objects.create(id=12345,first_name="Sally",last_name="Sparrow",username="crazy_girl",password="123",email="...com")
        u = User.objects.get(username='crazy_girl')
        u.set_password('123')
        u.save()
        Sport.objects.create(id=4,sport_name="Handball")
        s=Sport.objects.get(sport_name='Handball')
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
                "link":"asdd.com",
                "pathToEquipmentPostImage":None
                }
            }
        
        client=APIClient()
        client.login(username="crazy_girl", password="123")
        response = client.patch("/post/change_equipment_post/",data,format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)