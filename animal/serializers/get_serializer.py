# App
import email
from animal.models import Animal

# Framework
from rest_framework import serializers
from rest_framework.response import Response


class AnimalListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields= '__all__'
