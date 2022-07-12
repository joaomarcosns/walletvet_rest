# App
from users.models import User
from users.serializers.create_serializers import UserCreateSerializers
from users.serializers.get_serializers import UserListSerializers

# Framework
from rest_framework import viewsets



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializers
    
    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return UserCreateSerializers
        elif self.action == 'retrieve':
            pass
        return self.serializer_class
