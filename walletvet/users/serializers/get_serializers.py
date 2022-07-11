# App
import email
from users.models import User

# Framework
from rest_framework import serializers


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login', 'created_at', 'updated_at', 'is_active']

       