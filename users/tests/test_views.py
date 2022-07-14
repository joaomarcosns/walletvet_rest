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
        "password": "Teste123",
        "password_confirmation": "Teste123",
    }


class TestUser(APITestCase):
    def setUp(self):
        self.base_url = reverse('user-list')
        self.data = make_user()

    def test_user_creation_with_no_email_confirmation(self):
        """
        Testing user registry with invalid email
        """
        data = self.data
        data['email_confirmation'] = "any@gmail.com"
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email_confirmation'][0].code, "email_confirmation_must_match")

    def test_user_creation_invalid_password_confirmation(self):
        """
        Testing user registry with invalid password confirmation
        """
        data = self.data
        data['password_confirmation'] = "any123456"
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password_confirmation'][0].code, "password_confirmation_must_match")

    def test_user_creation_size_password(self):
        """
        Testing user registry with invalid password length
        """
        data = self.data
        data['password'] = "any"
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0].code, "password_size_min")

    def test_user_creation_birth_date_invalid(self):
        """
        Testing user registry with invalid birth date
        """
        data = self.data
        data['birth_date'] = "2023-12-23"
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['birth_date'][0].code, "birth_date_invalid")

    def test_user_creation_name_invalid(self):
        """
        Testing user registry with invalid name
        """
        data = self.data
        data["name"] = "Teste001"
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['name'][0].code, "name_invalid")