
from animal.models import (
    Animal,
    Breed
)
from animal.serializers.get_serializer import (
    AnimalListSerializers,
    BreedListSerializers
)

from rest_framework import viewsets
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalListSerializers
    permission_classes = [IsAuthenticated]


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedListSerializers
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get_queryset(self):
        queryset = self.queryset
        params = self.request.query_params
        fk = params.get('fk', None)
        if fk:
            queryset = queryset.filter(fk_type_animal_id=fk)
        return queryset
