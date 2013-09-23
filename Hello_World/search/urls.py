from django.conf.urls import patterns, url, include
from Hello_World.search import views
from Hello_World.search.api.views import ServiceAPI

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^autocomplete-search-city/$', views.autocomplete_city, name='autocomplete-search-city'),
	url(r'^api/$', ServiceAPI.as_view(), name='restaurant_list'),
)