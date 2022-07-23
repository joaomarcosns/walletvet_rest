# App
from animal.models import (
    Animal,
    Breed,
    Color,
    TypeAnimal
)
from users.serializers.get_serializers import UserListSerializers

# Framework
from rest_framework import serializers
from rest_framework.response import Response

class TypeAnimalListSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeAnimal
        fields= '__all__'


class BreedListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields= '__all__'


class AnimalListSerializers(serializers.ModelSerializer):
    fk_user = UserListSerializers()
    class Meta:
        model = Animal
        fields= "__all__"
        depth = 1

class ColorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields= '__all__'
        