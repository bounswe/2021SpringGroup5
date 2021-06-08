from django.test import TestCase
from .models import Sport
from django.urls import reverse
from django.contrib.auth.models import User


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
        fetched_sport = response.json()

        self.assertEqual(fetched_sport['id'], sport.id)
        self.assertEqual(fetched_sport['name'], sport.name)
        self.assertEqual(fetched_sport['description'], sport.description)
        self.assertEqual(response.status_code, 200)


class SimilarSportViewTests(TestCase):
    def test_invalid_id(self):
        """
        If id of sport which we wants to get similar sports is not in the database
        """
        create_sport(83)
        id = 2
        url = reverse('sport_relation:api-similar', args=[id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_retrieve_similar(self):
        """
        If retrieval of similar sport is correct
        """
        create_sport(83)
        id = 83
        url = reverse('sport_relation:api-similar', args=[id])
        response = self.client.get(url)
        similar_sports = response.json()

        self.assertTrue(isinstance(similar_sports, list))
        self.assertEqual(response.status_code, 200)


class SuggestSportViewTests(TestCase):
    def test_invalid_id(self):
        """
        If id of sports which we wants to get suggestion sports from them is not in the database
        """
        create_sport(83)
        id = "2"
        url = reverse('sport_relation:api-suggest',
                      args=['-'.join([id, id, id])])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_retrieve_similar(self):
        """
        If retrieval of suggestion is correct
        """
        create_sport(83)
        id = "83"
        url = reverse('sport_relation:api-suggest',
                      args=['-'.join([id, id, id])])
        response = self.client.get(url)
        suggestion = response.json()

        self.assertTrue(isinstance(suggestion, dict))
        self.assertEqual(response.status_code, 200)
