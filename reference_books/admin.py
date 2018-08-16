from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import (
    Unit,
    Manufacturer,
    Agriculture,
    Seed,
    Field,
    Fuel,
    WorkType,
    FarmingTechniques,
    Machinery,
    WorkAndTechnique,
)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'long_name',
        'short_name',
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Agriculture)
class AgricultureAdmin(admin.ModelAdmin):
    pass


@admin.register(Seed)
class SeedAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'agriculture',
        'manufacturer',
        'seeding_rate',
        'seeding_rate_unit',
    )
    list_filter = (
        'agriculture',
        'manufacturer',
    )


class BingGeoAdmin(OSMGeoAdmin):
    map_template = 'gis/admin/bing.html'


@admin.register(Field)
class FieldAdmin(BingGeoAdmin):
    default_lon = 3649825
    default_lat = 6349825
    default_zoom = 4
    map_width = 1000
    map_height = 600
    modifiable = True
    save_on_top = True


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(FarmingTechniques)
class FarmingTechniquesAdmin(admin.ModelAdmin):
    pass


@admin.register(Machinery)
class MachineryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'farming_techniques',
    )


@admin.register(WorkAndTechnique)
class WorkAndTechniqueAdmin(admin.ModelAdmin):
    list_display = (
        'work_type',
        'farming_techniques',
        'machinery',
        'fuel_rate',
        'fuel_rate_unit',
    )
    list_filter = (
        'work_type',
        'farming_techniques',
        'machinery',
    )
