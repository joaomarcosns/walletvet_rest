from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')

        user_data = {
            'name': "Teste",
            'is_active': True,
            'birth_date': "",
            'email': "teste@email.com",
            'password': "123456",
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
