from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class AirQualityTests(APITestCase):
    def test_invalid_user_id(self):
        data = {'user_id': 'asd'}
        client = APIClient()
        response = client.get('/api/pollution/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_id_not_found(self):
        data = {'user_id': '-1'}
        client = APIClient()
        response = client.get('/api/pollution/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_location(self):
        data = {'user_id': '5', 'latitude': '39.7667', 'longitude': '30.5256'}
        client = APIClient()
        response = client.post('/api/locations/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_location(self):
        client = APIClient()
        data = {'user_id': '5', 'latitude': '39.7667', 'longitude': '30.5256'}
        client.post('/api/locations/', data)
        data = {'user_id': '5'}
        response = client.get('/api/locations/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data[0].keys()), ['created', 'user_id', 'latitude', 'longitude'])

    def test_get_latest_pollution_of_user_location(self):
        client = APIClient()
        data = {'user_id': '5', 'latitude': '39.7667', 'longitude': '30.5256'}
        client.post('/api/locations/', data)
        data = {'user_id': '5'}
        response = client.get('/api/pollution/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data.keys()), ['aqi', 'name', 'color', 'description', 'polluiton_ts', 'city', 'state', 'country', 'coordinates'])