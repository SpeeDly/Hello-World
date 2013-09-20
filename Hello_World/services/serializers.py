from django.contrib.auth.models import User, Group
from Hello_World.services.models import Service
from Hello_World.location.models import Country
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url','username','email','groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url','name')

# class CountrySerializer(serializers.ModelSerializer):
# 	name = Country.name.title()
# 	class Meta:
# 		model = Country

class ServiceSerializer(serializers.ModelSerializer):
	country = serializers.RelatedField()
	town = serializers.RelatedField()
	class Meta:
		model = Service
#		depth = 2
'''
	country
	town
	name
	lat
	lng
	phone
	address
	postcode
'''