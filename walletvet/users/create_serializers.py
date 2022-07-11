# App
import email
from users.models import User

# Framework
from rest_framework import serializers


class UserCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login', 'created_at', 'updated_at', 'is_active']

    def create(self, validated_data):
        name = validated_data['name']
        email = validated_data['email']
        birth_date = validated_data['birth_date']
        password = validated_data['password']

        user_obj = {
            'name': name,
            'email': email,
            'birth_date': birth_date,
            'password': password
        }

        return user_obj
