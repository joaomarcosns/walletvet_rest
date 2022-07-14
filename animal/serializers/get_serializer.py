# App
from animal.models import (
    Animal,
    Breed,
    TypeAnimal
)

# Framework
from rest_framework import serializers
from rest_framework.response import Response


class AnimalListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields= '__all__'


class TypeAnimalListSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeAnimal
        fields= '__all__'


class BreedListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields= '__all__'
