# App
from users.models import User
from users.serializers.create_serializers import UserCreateSerializers

# Framework
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializers
