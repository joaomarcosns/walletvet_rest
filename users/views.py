# App
from users.models import User
from users.serializers.create_serializers import UserCreateSerializers
from users.serializers.get_serializers import UserListSerializers
from users.serializers.update_serializers import UserUpdateSerializers

# Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        request = self.request
        user_request = request.user
        if not user_request.is_superuser:
            queryset = queryset.filter(pk=user_request.pk)
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializers
        elif self.action == 'update':
            return UserUpdateSerializers
        elif self.action == 'retrieve':
            pass
        return self.serializer_class


