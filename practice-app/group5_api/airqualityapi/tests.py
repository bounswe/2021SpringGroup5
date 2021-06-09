from rest_framework import status
from rest_framework.test import APIClient, APITestCase



class AirQualityTests(APITestCase):

    # Tests if user id is not an integer
    def test_invalid_user_id(self):
        data = {'user_id': 'asd'}
        client = APIClient()
        response = client.get('/airQuality/api/pollution/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Tests if a user id is not found in location history
    def test_user_id_not_found(self):
        data = {'user_id': '-1'}
        client = APIClient()
        response = client.get('/airQuality/api/pollution/', data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # Tests adding a location and
    def test_add_location(self):
        data = {'user_id': '5', 'latitude': '39.7667', 'longitude': '30.5256'}
        client = APIClient()
        response = client.post('/airQuality/api/locations/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Creates a location and retrives it
    def test_get_location(self):
        client = APIClient()
        data = {'user_id': '5', 'latitude': '39.7667', 'longitude': '30.5256'}
        client.post('/airQuality/api/locations/', data)
        data = {'user_id': '5'}
        response = client.get('/airQuality/api/locations/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data[0].keys()), ['created', 'user_id', 'latitude', 'longitude'])

    # Creates a location and tests pollution for that location
    def test_get_latest_pollution_of_user_location(self):
        client = APIClient()
        data = {'user_id': '5', 'latitude': '39.7667', 'longitude': '30.5256'}
        client.post('/airQuality/api/locations/', data)
        data = {'user_id': '5'}
        response = client.get('/airQuality/api/pollution/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data.keys()), ['aqi', 'name', 'color', 'description', 'polluiton_ts', 'city', 'state', 'country', 'coordinates'])