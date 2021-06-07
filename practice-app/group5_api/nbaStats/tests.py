from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class nbaStats(APITestCase):

    # Tests if there is no player in this name
    def test_no_match(self):
        data = {"player_name": ""}
        client = APIClient()
        response = client.post("/nbaStats/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Tests if player name is valid and there will be match(es)
    def test_valid_player_name(self):
        data = {"player_name": "Davis"}
        client = APIClient()
        response = client.post("/nbaStats/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Tests if player name is meaningles and there is no match
    def test_valid_input(self):
        data = {"player_name": "asdasdasdasdasdasdasd"}
        client = APIClient()
        response = client.post("/nbaStats/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

