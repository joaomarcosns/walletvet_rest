from django.db import models
from django.utils.translation import gettext_lazy as _


class Color(models.Model):
    color = models.CharField(_('Color'), max_length=150)

    class Meta:
        db_table='color'

class HairType(models.Model):
    hair_type = models.CharField(_("Hair Type"), max_length=100)
    class Meta:
        db_table='hair_type'

class TypeAnimal(models.Model):
    type_animal = models.CharField(_("Type Animal"), max_length=100)
    class Meta:
        db_table='type_animal'

