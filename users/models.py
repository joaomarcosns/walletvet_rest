from typing import List
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

# OBS: This is the user/owner model


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('Name'), max_length=100)
    phone = models.CharField(_('Phone'), max_length=20)
    phone2 = models.CharField(_('Phone 2'), max_length=20, blank=True)
    city = models.CharField(_('City'), max_length=100)
    district = models.CharField(_('District'), max_length=200)
    street = models.CharField(_('street'), max_length=250)
    number = models.CharField(_('Number'), max_length=5)
    uf = models.CharField(_('UF'), max_length=2)
    email = models.EmailField(_('Email'), max_length=100, unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    birth_date = models.DateField(_('birth date'), auto_now_add=False)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = "email"

    REQUIRED_FIELDS = ['name','phone','phone2','city','district','street','number','uf','birth_date']

    def __str__(self) -> str:
        return super().__str__()
