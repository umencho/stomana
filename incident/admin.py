from django.contrib import admin
from .models import Incident, Area, TypeIncident
# Register your models here.
admin.site.register(Incident)
admin.site.register(Area)
admin.site.register(TypeIncident)
