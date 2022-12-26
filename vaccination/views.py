# App
from django import db
from vaccination.models import (
    Vaccination,
    Vaccine
)
from vaccination.serializers.get_serializer import	(
    VaccinationListSerializers,
    VaccineListSerializers
)
from vaccination.serializers.create_serializers import VaccinationCreateSerializers
# Framework
from rest_framework import viewsets
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.permissions import IsAuthenticated

class VaccinationViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationListSerializers
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return VaccinationCreateSerializers
        return self.serializer_class

class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineListSerializers
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get_queryset(self):
        queryset = self.queryset
        params = self.request.query_params
        fk = params.get('fk', None)
        if fk:
            queryset = queryset.filter(fk_type_animal_id=fk)
        return queryset

