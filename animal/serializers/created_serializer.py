#App
from animal.models import (
    Animal
)
# Framework
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class AnimalCreatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields= '__all__'

    def validate_name(self, value):
        if any(chr.isdigit() for chr in value):
            raise serializers.ValidationError(_("Invalid name entered"), "name_invalid")
        return value

    def create(self, validated_data):
        animal = Animal.objects.create(**validated_data)
        animal.save()
        return animal