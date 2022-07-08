# App
import email
from users.models import User

# Framework 
from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email','last_login', 'is_active', 'created_at', 'updated_at']


    def create(self, validated_data):
        name = validated_data['name']
        email = validated_data['email']
        is_active = validated_data['is_active']
        # return super().create(validated_data)


