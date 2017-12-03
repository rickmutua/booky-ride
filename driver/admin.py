from django.contrib import admin

from .models import DriverProfile, Place

# Register your models here.

admin.site.register(DriverProfile)

admin.site.register(Place)
