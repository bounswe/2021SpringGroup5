from django.test import TestCase
from .models import Sport
from django.urls import reverse


def create_sport(id):
    return Sport.objects.create(id=id, name="test", description="desc test")


class SportDetailViewTests(TestCase):
    def test_invalid_id(self):
        """
        If id of sport is not in the database
        """
        create_sport(1)
        id = 2
        url = reverse('sport_relation:api-sports', args=[id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_retrieve_sport(self):
        """
        If retrieval of sport is correct
        """
        sport = create_sport(1)
        id = 1
        url = reverse('sport_relation:api-sports', args=[id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(sport.name, response.json()['name'])


class SimilarSportViewTests(TestCase):
    def test_invalid_id(self):
        """
        If id of sport which we wants to get similar sports is not in the database
        """
        create_sport(1)
        id = 2
        url = reverse('sport_relation:api-similar', args=[id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_similar_less_than_5(self):
        """
        Number of similart sports are less than 5
        """
        create_sport(1)
        id = 1
        url = reverse('sport_relation:api-similar', args=[id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
