
from animal.models import Animal


from rest_framework import viewsets
from animal.serializers.get_serializer import AnimalListSerializers
from rest_framework.permissions import IsAuthenticated


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalListSerializers
    permission_classes = [IsAuthenticated]
