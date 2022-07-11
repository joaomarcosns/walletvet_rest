from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

#OBS reverse tem quer ser nome do App-método (Ex: list, created, etc)
class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('users-list')
        user_data = {
            "password": "Teste",
            "name": "Teste",
            "phone": "+1 (408) 233-3278",
            "phone2": "+1 (445) 498-2203",
            "city": "Teste",
            "district": "Teste",
            "street": "Teste",
            "number": "468",
            "uf": "To",
            "email": "rebyqon@mailinator.com",
            "birth_date": "1975-10-27"
        }

    def tearDown(self):
        return super().tearDown()
