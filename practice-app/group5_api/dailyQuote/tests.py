import requests
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


# Warning: The remote API allows up to a limit of requests per hour.
# This does not effect the functionality of the API as we use the quote in database if that happens.
# However, this causes the tests to fail (returning 404) if that happens.
# So the tests should be run making sure that limit is not exceeded.

class DailyQuoteTests(APITestCase):

    # test if get method works correctly
    def test_get(self):
        client = APIClient()
        response = client.get("/dailyQuote/api/")
        remote_response = requests.get('https://quotes.rest/qod?category=sports&language=en')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # response body containts quote_text, author, value and ratings
        body = response.json()["response"]
        self.assertIn("quote_text", body)
        self.assertIn("author", body)
        self.assertIn("value", body)
        self.assertIn("ratings", body)
        # as the quote is just created, value and ratings are both 0
        self.assertEqual(body["value"], 0)
        self.assertEqual(body["ratings"], 0)

        # the response's quote_text and author should match with remote api's
        remote_body = remote_response.json()["contents"]["quotes"][0]
        self.assertEqual(remote_body['quote'], body['quote_text'])
        self.assertEqual(remote_body['author'], body['author'])

    def test_post_invalid_input(self):
        # first, send a get request to create a quote in the database
        client = APIClient()
        response = client.get("/dailyQuote/api/")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # the points can't be greater than 5
        data = {"Points": 10}
        client = APIClient()
        response = client.post("/dailyQuote/api/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # the points can't be lower than 5
        data = {"Points": -1}
        client = APIClient()
        response = client.post("/dailyQuote/api/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # the points can't be real numbers
        data = {"Points": 1.5}
        client = APIClient()
        response = client.post("/dailyQuote/api/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # the points can't be strings
        data = {"Points": 'points'}
        client = APIClient()
        response = client.post("/dailyQuote/api/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # the request body should contain the key 'Points'
        data = {}
        client = APIClient()
        response = client.post("/dailyQuote/api/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post(self):
        # first, send a get request to create a quote in the database
        client = APIClient()
        response = client.get("/dailyQuote/api/")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # send a post request
        points_1 = 5
        data = {"Points": points_1}
        client = APIClient()
        response = client.post("/dailyQuote/api/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # as only one post request is made, the ratings should equal 1 and the value should equal the calculated value
        body = response.json()["response"]
        self.assertIn("value", body)
        self.assertIn("ratings", body)
        self.assertEqual(body["value"], "{:.1f}".format(points_1 * 1.0 / 1))
        self.assertEqual(body["ratings"], 1)

        # send a second post request
        points_2 = 3
        data = {"Points": points_2}
        client = APIClient()
        response = client.post("/dailyQuote/api/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # as two post requests are made, the ratings should equal 2 and the value should equal the calculated average
        body = response.json()["response"]
        self.assertIn("value", body)
        self.assertIn("ratings", body)
        self.assertEqual(body["value"], "{:.1f}".format((points_1 + points_2) * 1.0 / 2))
        self.assertEqual(body["ratings"], 2)
