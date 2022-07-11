# App
from users.create_serializers import UserCreateSerializers
from users.models import User

# Framework
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializers
