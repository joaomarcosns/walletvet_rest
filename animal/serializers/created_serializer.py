#App
from animal.models import (
    Animal
)
# Framework
from rest_framework import serializers
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta
from django.utils.translation import gettext_lazy as _

class AnimalCreatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields= '__all__'

    def validate_name(self, value):
        if any(chr.isdigit() for chr in value):
            raise serializers.ValidationError(_("Invalid name entered"), "name_invalid")
        return value

    def validate_birth_date(self, value):
        difference = relativedelta(now().date(),value)
        if difference.days < 0:
            raise serializers.ValidationError(_("User must be over 18 years old"), "birth_date_invalid")
        return value

    def create(self, validated_data):
        animal = Animal.objects.create(**validated_data)
        animal.save()
        return animal