from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class UmutAPITests(APITestCase):
    def test_add_category(self):
        client = APIClient()
        data = {'category_name': 'Deneme Categori Name', 'category_description': 'Deneme Categori Description', 'max_player': 100,}
        client.post('/umutAPI/add/category/', data)
        response = client.get('/umutAPI/add/category/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category(self):
        client = APIClient()
        data = {'category_name': 'Deneme Categori Name'},
        client.post('/umutAPI/category/', data)
        response = client.get('/umutAPI/category/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_category(self):
        client = APIClient()
        data = {}
        client.post('/umutAPI/category/', data)
        response = client.get('/umutAPI/category/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_category(self):
        client = APIClient()
        data = {'category_name': '-1'}
        response = client.get('/umutAPI/category/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)