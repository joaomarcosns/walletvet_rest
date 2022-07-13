from django.db import models
from django.utils.translation import gettext_lazy as _


class TypeAnimal(models.Model):
    type_animal = models.CharField(_("Type Animal"), max_length=100)
    class Meta:
        db_table='type_animal'
