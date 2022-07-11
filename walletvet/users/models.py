from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# OBS: This is the user/owner model

class User(AbstractBaseUser):
    name = models.CharField('Name', max_length=100)
    phone = models.CharField('Phone', max_length=20)
    phone2 = models.CharField('Phone 2', max_length=20)
    city = models.CharField('City', max_length=100)
    district = models.CharField('District', max_length=200)
    street = models.CharField('street', max_length=250)
    number = models.CharField('Number', max_length=5)
    uf = models.CharField('UF', max_length=2)
    email = models.EmailField('Email', max_length=100, unique=True)
    is_active = models.BooleanField('active', default=True)
    birth_date = models.DateField("birth date", auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return super().__str__() 