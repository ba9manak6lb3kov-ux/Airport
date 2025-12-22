from django.contrib import admin

from django.contrib import admin
from .models import City, Flight

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "latitude", "longitude")
    search_fields = ("name", "region")

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ("airline", "origin", "destination", "departure_time", "arrival_time", "status")
    list_filter = ("airline", "origin", "destination", "status")
    search_fields = ("airline",)
