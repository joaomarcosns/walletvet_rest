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
        # name = validated_data['name']
        # birth_date = validated_data['birth_date']
        # phone =  validated_data['phone']
        # phone2 =  validated_data['phone2']
        # city =  validated_data['city']
        # district =  validated_data['district']
        # street =  validated_data['street']
        # number =  validated_data['number']
        # uf =  validated_data['uf']
        # email = validated_data['email']
        # password = validated_data['password']


        return User.objects.create(**validated_data)
