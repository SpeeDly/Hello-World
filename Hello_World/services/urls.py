from django.conf.urls import patterns, url, include
from rest_framework import routers
from Hello_World.services import views

router = routers.DefaultRouter()
router.register(r'services', views.ServiceViewSet)
urlpatterns = patterns('',
    url(r'^', include(router.urls)),

)