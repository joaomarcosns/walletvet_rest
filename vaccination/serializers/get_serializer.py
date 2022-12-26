# App
from vaccination.models import (
    Vaccination, 
    Vaccine,
)

# Framework
from rest_framework import serializers
from rest_framework.response import Response


class VaccinationListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields= '__all__'
        depth = 1


class VaccineListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields= '__all__'

