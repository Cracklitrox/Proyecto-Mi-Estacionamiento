from django.contrib import admin
from .models import Region, Provincia, Comuna

# Register your models here.

admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)