
from animal.models import (
    Animal,
    Breed,
    Color,
    TypeAnimal
)
from animal.serializers.get_serializer import (
    AnimalListSerializers,
    BreedListSerializers,
    ColorListSerializers,
    TypeAnimalListSerializers
)

from animal.serializers.created_serializer import (
    AnimalCreatedSerializer
)

from rest_framework import viewsets
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class TypeAnimalViewSet(viewsets.ModelViewSet):
    queryset = TypeAnimal.objects.all()
    serializer_class = TypeAnimalListSerializers
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalListSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        request = self.request
        user = request.user
        return queryset.filter(fk_user_id=user.pk)

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return AnimalCreatedSerializer
        return self.serializer_class


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

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorListSerializers
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']
    
