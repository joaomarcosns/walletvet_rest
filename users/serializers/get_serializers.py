# App
import email
from users.models import User

# Framework
from rest_framework import serializers
from rest_framework.response import Response


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'user_permissions', 'groups', 'is_superuser', "is_staff"]

       