# App
from django import db
from animal.models import (
    TypeAnimal,
    Animal
)
# Framework
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Vaccine(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    fk_type_animal = models.ForeignKey(TypeAnimal, on_delete=models.CASCADE)

    class Meta:
        db_table='vaccine'

    def __str__(self) -> str:
        return self.name

class Vaccination(models.Model):
    fk_vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    vaccine_dose = models.IntegerField(_("Vaccine Dose"))
    batch = models.CharField(_("Batch"), max_length=150)
    date_vaccination = models.DateTimeField(_("Date Vaccine"))
    date_return = models.DateTimeField(_("Date Return"))
    responsible = models.CharField(_("Responsible"), max_length=150)
    fk_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)

    class Meta:
        db_table='vaccination'

    def __str__(self) -> str:
        return '{fk_animal} {pk_vaccine}'.format(fk_animal=self.fk_animal, pk_vaccine=self.pk_vaccine)
