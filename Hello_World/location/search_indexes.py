from haystack import indexes
from Hello_World.location.models import Town


class TownIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True)
	name = indexes.NgramField(model_attr='name')
	
	def get_model(self):
		return Town