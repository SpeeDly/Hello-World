from django.contrib.gis.db import models


class Country(models.Model):
	name = models.CharField(max_length=500)
	def __unicode__(self):
		return self.name.title()


class Town(models.Model):
	name = models.CharField(max_length=500)
	country = models.ForeignKey(Country)
	def __unicode__(self):
		return self.name