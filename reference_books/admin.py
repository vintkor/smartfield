from django.contrib.gis import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import (
    Currency,
    Unit,
    Manufacturer,
    Agriculture,
    Seed,
    Field,
    Fuel,
    FuelCoast,
    WorkType,
    FarmingTechniques,
    Machinery,
    WorkAndTechnique,
    Fertilizer,
    Protection,
    AdditionalExpenditure,
    FarmingTechniquesType,
    MachineryType,
    ProcessCycle,
)
from django.conf import settings


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'iso_4217_letter_code',
        'iso_4217_numeric_code',
        'short_symbol',
        'is_main',
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


@admin.register(FuelCoast)
class FuelCoastAdmin(admin.ModelAdmin):
    list_display = (
        'fuel',
        'price',
        'created',
    )
    list_filter = ('fuel',)


class FuelCoastInline(admin.TabularInline):
    extra = 0
    model = FuelCoast


@admin.register(Field)
class FieldAdmin(admin.OSMGeoAdmin):
    map_template = 'gis/admin/google.html'
    extra_js = [
        'https://maps.googleapis.com/maps/api/js?key={0}'.format(settings.GOOGLE_MAPS_API_KEY),
    ]
    map_width = 1200
    map_height = 700
    save_on_top = True
    modifiable = True
    default_lon = 3503050
    default_lat = 6278821
    default_zoom = 6

    list_display = (
        'title',
        'square',
        'square_unit',
        'rent_cost',
        'rent_cost_unit',
        'rent_cost_currency',
    )


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    inlines = (
        FuelCoastInline,
    )


@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_editable = ('sort',)
    list_display = ('title', 'sort')
    filter_horizontal = ('units',)


@admin.register(FarmingTechniquesType)
class FarmingTechniquesTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(MachineryType)
class MachineryTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(FarmingTechniques)
class FarmingTechniquesAdmin(admin.ModelAdmin):
    pass


@admin.register(Machinery)
class MachineryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    filter_horizontal = ('farming_techniques',)


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


@admin.register(Fertilizer)
class FertilizerAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'manufacturer',
    )


@admin.register(Protection)
class ProtectionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'manufacturer',
    )


@admin.register(AdditionalExpenditure)
class AdditionalExpenditureAdmin(admin.ModelAdmin):
    pass


@admin.register(ProcessCycle)
class ProcessCycleAdmin(admin.ModelAdmin):
    pass
