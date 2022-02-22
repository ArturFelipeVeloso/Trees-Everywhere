from django.contrib import admin
from .models import Plant, PlantedTrees

@admin.register(PlantedTrees)
class PlantedTreesAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'planted_at', 'tree', 'location_lat', 'location_long')

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name')