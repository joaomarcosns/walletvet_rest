from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.core.files.uploadedfile import SimpleUploadedFile


from users.models import User
from animal.models import (
    TypeAnimal,
    Color,
    Breed,
    Animal
)

from vaccination.models import (
    Vaccine
)

# OBS reverse tem quer ser nome do App-método (Ex: list, created, etc)


def make_vaccination():
    small_gif = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
        b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
        b'\x02\x4c\x01\x00\x3b'
    )
    # User
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
    # TypeAnimal
    make_type_animal = TypeAnimal.objects.create(
        type_animal='cat'
    )
    # Breed
    make_breed = Breed.objects.create(
        breed="TEste",
        fk_type_animal=make_type_animal
    )
    make_breed.save()
    # Color
    make_color = Color.objects.create(
        color='red'
    )
    make_color.save
    # Animal
    make_animal = Animal.objects.create(
        name ="Tay",
        birth_date ="2021-07-14",
        gender ="M",
        description ="TESTE",
        photo=SimpleUploadedFile(
            'small.gif', small_gif, content_type='image/gif'),
        hair_type ="M",
        fk_breed_id =make_breed.pk,
        fk_color_id =make_color.pk,
        fk_type_animal_id=make_type_animal.pk,
        fk_user_id=make_user.pk
    )
    make_animal.save()
    # Vaccine
    make_vaccine = Vaccine.objects.create(
        name='V3',
        fk_type_animal_id = make_type_animal.pk,
    )
    make_vaccine.save()

    return {
        "vaccine_dose": 1,
        "batch": "XXX9-054054-0541054",
        "date_vaccination": "2022-07-16",
        "date_return": "2023-07-16",
        "responsible": "TESTE",
        "fk_vaccine": make_vaccine.pk,
        "fk_animal": make_animal.pk,
    }


class TestVaccination(APITestCase):
    def setUp(self):
        self.base_url = reverse('vaccination-list')
        self.data = make_vaccination()
        login = self.client.login(
            email='rebyqon@mailinator.com', password='Teste123')

    def test_vaccination_creation_responsible_invalid(self):
        """
        Testing vaccination registry with invalid responsible
        """
        data = self.data
        data['responsible'] = "TESTE001"
        response = self.client.post(self.base_url, data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['responsible'][0].code, "responsible_invalid")
