import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

class PersonTests(TestCase):
    def setUp(self):
        Person.objects.create(first_name='Kulnev', last_name='Oleg')

    def test_person_create(self):
        person_kulnev_oleg = Person.objects.get(first_name='Kulnev')
        self.assertEqual(person_kulnev_oleg.first_name, 'Kulnev')

class PersonViewTest(APITestCase):
    client = APIClient()
    url = reverse('get_post_person')

    def setUp(self):
        Person.objects.create(first_name='Kulnev', last_name='Oleg')
        Person.objects.create(first_name='Napreev', last_name='Sergey')
        Person.objects.create(first_name='Malcov', last_name='Egor')

    def test_get_all_persons(self):

        persons = Person.objects.all()
        serialized = PersonSerializer(persons, many=True)

        response = self.client.get(self.url)
        self.assertEqual(serialized.data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_add_new_person(self):
        person = {
                'first_name': 'Savostyanov',
                'last_name': 'Vitaliy',
        }

        response = self.client.post(self.url,data=json.dumps(person),content_type='application/json')

        self.assertEqual(response.data, person)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

