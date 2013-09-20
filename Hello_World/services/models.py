from django.contrib.gis.db import models
from Hello_World.location.models import *


class ServiceType(models.Model):
	name = models.CharField(max_length=500)
	def __unicode__(self):
		return self.name


class Service(models.Model):
	country = models.ForeignKey(Country)
	town = models.ForeignKey(Town)
	service_type = models.ForeignKey(ServiceType)
	name = models.CharField(max_length=500)
	lat = models.FloatField()
	lng = models.FloatField()
	phone = models.CharField(max_length=500)
	address = models.CharField(max_length=500)
	postcode = models.CharField(max_length=500)
	def __unicode__(self):
		return self.name