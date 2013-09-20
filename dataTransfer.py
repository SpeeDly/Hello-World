import pymongo
from pymongo import MongoClient
from django.core.management import setup_environ
from Hello_World import settings
setup_environ(settings)
from Hello_World.services.models import *
from Hello_World.location.models import *
import Hello_World


DB_NAMES_BLACKLIST = ['local', 'crawling', 'restaurants']
DB_COLLECTION_NAMES_BLACKLIST = ['system.indexes', 'towns']


client = MongoClient('mongodb://ec2-54-216-43-232.eu-west-1.compute.amazonaws.com/')
countries = client.database_names()


for country in countries:
	if country == 'germany':
		if not country.split("_")[0] in DB_NAMES_BLACKLIST:
			db = client[country]
			services = db.collection_names()
			towns = db.towns
			new_country = Country(name=country)
			new_country.save()
			for service in services:
				if not service == "System.Indexes":
					service_name = service.replace('_', ' ').title()
					new_service_type = ServiceType(name=service_name)
					new_service_type.save()
					if not service in DB_COLLECTION_NAMES_BLACKLIST:
						current_services = db[service]
						for current_service in current_services.find():

							country = country.replace('_',' ').title()
							town = current_service.get('town')
							name = current_service.get('name')
							geolocation = current_service.get('geolocation')
							phone = current_service.get('phone')
							address = current_service.get('address')
							postcode = current_service.get('postcode')

							if all([name, town, geolocation, phone, address, postcode]):

								current_town = Town(name=towns.find_one({"_id": town})['name'], country=new_country)
								new_town = Town.objects.filter(name=current_town.name)
								if not new_town:
									current_town.save()
									new_town = Town.objects.filter(name=current_town.name)

								# current_service_type = ServiceType(name=services.find_one({"_id": town})['name'])
								# new_service_type = ServiceType.objects.filter(name=current_service_type.name)
								# if not new_service_type:
								# 	new_service_type.save()
								# 	new_service_type = ServiceType.objects.filter(name=new_service_type.name)

								new_service = Service(
									country=new_country,
									town=new_town[0],
									service_type=new_service_type,
									name=name,
									lat=geolocation['lat'],
									lng=geolocation['lng'],
									phone=phone,
									address=address,
									postcode=postcode
									)
								new_service.save()