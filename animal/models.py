from django.db import models
from django.utils.translation import gettext_lazy as _

class TypeAnimal(models.Model):
    type_animal = models.CharField(_("Type Animal"), max_length=100)
    class Meta:
        db_table='type_animal'

class Breed(models.Model):
    breed = models.CharField(_("Breed"), max_length=200)
    fk_type_animal = models.ForeignKey(_("Type Animal"), TypeAnimal)
    class Meta:
        db_table='breed'

