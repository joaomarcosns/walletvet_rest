# App
from users.models import User

# Framework
from rest_framework import serializers
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta
from django.utils.translation import gettext_lazy as _

class UserCreateSerializers(serializers.ModelSerializer):
    email_confirmation = serializers.EmailField(required=True, write_only=True)
    password_confirmation = serializers.CharField(required=True, write_only=True)

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
            'email',
            'email_confirmation',
            'password',
            'password_confirmation',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_email_confirmation(self, value):
        data = self.get_initial()
        email = data.get('email')
        if value != email:
            raise serializers.ValidationError(_("Emails must match"), "email_confirmation_must_match")
        return value

    def validate_password_confirmation(self, value):
        data = self.get_initial()
        password = data.get('password')
        if value != password:
            raise serializers.ValidationError(_("Password must match"), "password_confirmation_must_match")
        return value

    def validate_password(self, value):
        data = self.get_initial()
        if len(data.get('password')) < 6:
            raise serializers.ValidationError(_("Password must be longer than 6 characters"),
             "password_size_min")
        return value

    def validate_birth_date(self, value):
        difference = relativedelta(now().date(),value)
        if difference.years < 18:
            raise serializers.ValidationError(_("User must be over 18 years old"), "birth_date_invalid")
        return value

    def validate_name(self, value):
        if any(chr.isdigit() for chr in value):
            raise serializers.ValidationError(_("Invalid name entered"), "name_invalid")
        return value


    def create(self, validated_data):
        del validated_data["email_confirmation"]
        del validated_data["password_confirmation"]
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
