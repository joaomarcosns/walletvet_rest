from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.core.files.uploadedfile import SimpleUploadedFile


from users.models import User
from ..models import (
    TypeAnimal,
    Color,
    Breed
)

# OBS reverse tem quer ser nome do App-método (Ex: list, created, etc)


def make_animal():
    small_gif = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
        b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
        b'\x02\x4c\x01\x00\x3b'
    )
    make_user = User.objects.create_user(
        name="Teste",
        birth_date="1975-10-27",
        phone="+1 (408) 233-3278",
        phone2="+1 (445) 498-2203",
        city="Teste",
        district="Teste",
        street="Teste",
        number="468",
        uf="To",
        email="rebyqon@mailinator.com",
        password="Teste123",
    )
    make_user.save()
    make_type_animal = TypeAnimal.objects.create(
        type_animal='cat'
    )
    make_breed = Breed.objects.create(
        breed="TEste",
        fk_type_animal=make_type_animal
    )
    make_breed.save()
    make_color = Color.objects.create(
        color='red'
    )
    make_color.save

    return {
        "name": "Tay",
        "birth_date": "2021-07-14",
        "gender": "M",
        "description": "TESTE",
        "photo": SimpleUploadedFile('small.gif', small_gif, content_type='image/gif'),
        "hair_type": "M",
        "fk_breed": make_breed.pk,
        "fk_color": make_color.pk,
        "fk_type_animal": make_type_animal.pk,
        "fk_user": make_user.pk
    }


class TestUser(APITestCase):
    def setUp(self):
        self.base_url = reverse('animal-list')
        self.data = make_animal()
        login = self.client.login(
            email='rebyqon@mailinator.com', password='Teste123')

    def test_animal_creation_name_invalid(self):
        """
        Testing animal registry with invalid name
        """
        data = self.data
        data['name'] = "TESTE001"
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['name'][0].code, "name_invalid")

    def test_animal_creation_birth_date_invalid(self):
        """
        Testing animal registry with invalid birth date
        """
        data = self.data
        data['birth_date'] = "2022-07-15"
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['birth_date'][0].code, "birth_date_invalid")