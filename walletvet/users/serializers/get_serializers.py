# App
import email
from users.models import User

# Framework
from rest_framework import serializers


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

       