from django.contrib import admin
from .models import Room, AQThermalUnit, Measurement

admin.site.register(Room)
admin.site.register(AQThermalUnit)
admin.site.register(Measurement)
