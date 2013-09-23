from Hello_World.services.models import Service
from rest_framework import viewsets
from Hello_World.services.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer