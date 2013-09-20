from django.conf.urls import patterns, url, include
from Hello_World.search import views


urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^autocomplete-search-city/$', views.autocomplete_city, name='autocomplete-search-city'),
	url(r'^api/$', api.views, name='api'),
)