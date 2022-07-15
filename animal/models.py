from users.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

class Color(models.Model):
    color = models.CharField(_('Color'), max_length=150)

    class Meta:
        db_table='color'

    def __str__(self) -> str:
        return self.color

class TypeAnimal(models.Model):
    type_animal = models.CharField(_("Type Animal"), max_length=100)
    class Meta:
        db_table='type_animal'
    
    def __str__(self) -> str:
        return self.type_animal

class Breed(models.Model):
    breed = models.CharField(_("Breed"), max_length=200)
    fk_type_animal = models.ForeignKey(TypeAnimal, on_delete=models.CASCADE)
    class Meta:
        db_table='breed'

    def __str__(self) -> str:
        return self.breed

class Animal(models.Model):
    GENDER_CHOICES = (
        ("F", "Female"),
        ("M", "Male")
    )
    HAIR_TYPE_CHOICES = (
        ("S", "Small"),
        ("M", "Mid"),
        ("L", "Large")
    )
    name = models.CharField(_('Name'), max_length=100)
    birth_date = models.DateField(_('birth date'), auto_now_add=False)
    gender = models.CharField(_("Gender"), max_length=1, choices=GENDER_CHOICES, blank=False, null=False)
    description = models.TextField(_('Description'), max_length=999, blank=True)
    photo = models.ImageField(_('photo'), blank=True)
    hair_type = models.CharField(_("hair Type"), max_length=1, choices=HAIR_TYPE_CHOICES, blank=False, null=False)
    fk_breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    fk_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    fk_type_animal = models.ForeignKey(TypeAnimal, on_delete=models.CASCADE)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table='animal'

    def __str__(self) -> str:
        return self.name
