from haystack import indexes
from Hello_World.services.models import Service


class SearchIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True)
	country = indexes.CharField(model_attr='country')
	town = indexes.CharField(model_attr='town')
	name = indexes.CharField(model_attr='name')
	service_type = indexes.CharField(model_attr='service_type')
	
	def get_model(self):
		return Service