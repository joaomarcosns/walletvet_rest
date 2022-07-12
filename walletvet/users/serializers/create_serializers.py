# App
from users.models import User

# Framework
from rest_framework import serializers


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
            raise serializers.ValidationError("Emails must match", "email_confirmation_must_match")
        return value

    def validate_password_confirmation(self, value):
        data = self.get_initial()
        password = data.get('password')
        if value != password:
            raise serializers.ValidationError("Password must match", "password_confirmation_must_match")
        return value

    def create(self, validated_data):
        del validated_data["email_confirmation"]
        del validated_data["password_confirmation"]
        # data['password'] = User.set_password(data['password'])
        return User.objects.create(**validated_data)
