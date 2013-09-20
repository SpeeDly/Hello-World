from django.conf import settings
from pyelasticsearch import ElasticSearch


class SearchModel(object):


	def __init__(self):
		connection_url = settings.HAYSTACK_CONNECTIONS['default']['URL']
		self.index = settings.HAYSTACK_CONNECTIONS['default']['INDEX_NAME']
		self.elastic = ElasticSearch(connection_url)


	def find(self, field=None, term=None):
		search  = self.elastic.search('{0}:{1}'.format(field, term), index=self.index,)

		results = None
		hits = search.get('hits', None)

		if hits != None:
			results = hits.get('hits', None)

		return results


search_model = SearchModel()