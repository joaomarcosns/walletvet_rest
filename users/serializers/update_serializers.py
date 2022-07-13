# App
from users.models import User

# Framework
from rest_framework import serializers
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta


class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'birth_date',
            'phone',
            'phone2',
            'city',
            'district',
            'street',
            'number',
            'uf',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_birth_date(self, value):
        difference = relativedelta(now().date(),value)
        if difference.years < 18:
            raise serializers.ValidationError("User must be over 18 years old", "birth_date_invalid")
        return value

    
