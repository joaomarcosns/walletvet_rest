from django.db import models
from django.utils.translation import gettext_lazy as _



class Color(models.Model):
    color = models.CharField(_('Color'), max_length=150)
