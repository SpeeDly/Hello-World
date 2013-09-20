from django.conf.urls import patterns, url, include
from rest_framework import routers
from Hello_World.services import views

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'services', views.ServiceViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    #url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
)