from Hello_World.services.models import Service
from Hello_World.location.models import Country
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
	country = serializers.RelatedField()
	town = serializers.RelatedField()
	class Meta:
		model = Service
