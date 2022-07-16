# App
from vaccination.models import Vaccination
# Framework
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _



class VaccinationCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = '__all__'

    def validate_responsible(self, value):
        if any(chr.isdigit() for chr in value):
            raise serializers.ValidationError(_("Invalid responsible entered"), "responsible_invalid")
        return value

    def validate_date_vaccination(self, attrs):
        if attrs > now():
            raise serializers.ValidationError(_("More than current data"), "date_vaccination_invalid")
        return super().validate(attrs)
    
    def create(self, validated_data):
        vaccination = Vaccination.objects.create(**validated_data)
        vaccination.save()
        return vaccination
