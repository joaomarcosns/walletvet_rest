# App
from animal.models import TypeAnimal
# Framework
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Vaccine(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    pk_type_animal = models.ForeignKey(TypeAnimal, on_delete=models.SET_NUll, null=True)

    class Meta:
        db_table='Vaccine'

    def __str__(self) -> str:
        return self.name