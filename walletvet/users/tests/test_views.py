from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_400_BAD_REQUEST

# OBS reverse tem quer ser nome do App-método (Ex: list, created, etc)


def make_user():
    return {
        "name": "Teste",
        "birth_date": "1975-10-27",
        "phone": "+1 (408) 233-3278",
        "phone2": "+1 (445) 498-2203",
        "city": "Teste",
        "district": "Teste",
        "street": "Teste",
        "number": "468",
        "uf": "To",
        "email": "rebyqon@mailinator.com",
        "email_confirmation": "rebyqon@mailinator.com",
        "password": "Teste",
    }


class TestUser(APITestCase):
    def setUp(self):
        self.base_url = reverse('user-list')
        self.data = make_user()

    def test_user_creation_with_no_email_confirmation(self):
        """
        Testing user registration without confirming the email
        """
        data = self.data
        data['email_confirmation'] = "any@gmail.com"
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data['email_confirmation'][0].code, "email_confirmation_must_match")
