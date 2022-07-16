from django.contrib import admin
from .models import (
    Vaccination,
    Vaccine
)
# Register your models here.

class VaccineShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pk_type_animal')
    list_filter = ('name', 'pk_type_animal',)
    search_fields = ('name', )

class VaccinationShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'pk_vaccine', 'fk_animal')
    list_display = ('pk_vaccine', 'fk_animal', )
    search_fields = ('fk_animal', 'pk_vaccine', )


admin.site.register(Vaccination, VaccinationShowAdmin)
admin.site.register(Vaccine, VaccineShowAdmin)