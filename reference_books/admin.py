from django.contrib import admin
from .models import (
    Unit,
    Manufacturer,
    Agriculture,
    Seed,
)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass


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
