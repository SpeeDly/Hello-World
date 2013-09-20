from annoying.decorators import render_to
from django.utils import simplejson
from django.http import HttpResponse
from django.template import RequestContext, loader
from Hello_World.services.models import *
from Hello_World.location.models import *
from Hello_World.search.search import search_model
from Hello_World.search.forms import SimpleForm
from haystack.query import SearchQuerySet


SELECT_OPTIONS = ('town', 'name')


@render_to('index.html')
def index(request):
	service_types = ServiceType.objects.all()[1:]
	form = SimpleForm(request.GET)
	
	simple_form = []
	search = ''
	search_by = 0
	results = []
	counts = []
	names_and_types = []
	all_count = 0

	if form.is_valid():
		simple_form = form.cleaned_data['service_types']
		search = form.cleaned_data['search']
		search_by = form.cleaned_data['select']

	if not simple_form:
		for s in service_types:
			simple_form.append(s.name)

	if search_by and request.method == 'GET':
		search_by = SELECT_OPTIONS[int(search_by)]
		if search_by == 0:
			results = SearchQuerySet().models(Service).filter(town=search)
		else:
			results = SearchQuerySet().models(Service).filter(name=search)
		results_count = results
		results = results.filter(service_type__in=simple_form)

	for r in results:
		names_and_types.append((r.name,r.service_type,r.town))
	
	if search_by:
		for r in results_count:
				counts.append((r.service_type ,results_count.filter(service_type=r.service_type).count()))

		counts = set(counts)
		temp = []
		for x, y in counts:
			temp.append(x)
			if x in simple_form:
				all_count = all_count + y
		
		for service_type in service_types:
			if not service_type.name in temp:
				counts.add((service_type.name, 0))

	return {'names_and_types':names_and_types, 'service_types': service_types, 'form': form, 'counts': counts, 'all_count': all_count}



def autocomplete_city(request):

	search = request.GET.get('term', None)

	results = SearchQuerySet().models(Town).filter(name__startswith=search).order_by('-_score')[:20]
	suggestions = []

	if results:
		for r in results:
			suggestions.append({"value": r.name})

	return HttpResponse(simplejson.dumps(suggestions), content_type="application/json")