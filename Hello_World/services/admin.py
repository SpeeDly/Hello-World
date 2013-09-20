from django.contrib import admin
from Hello_World.services.models import *
from Hello_World.location.models import *

admin.site.register(Town)
admin.site.register(Country)
admin.site.register(ServiceType)

class ServiceAdmin(admin.ModelAdmin):
	list_filter = ('service_type', )
	list_display = ('id', 'service_type', 'name')
	
admin.site.register(Service, ServiceAdmin)