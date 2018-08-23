from django.contrib import admin
from .models import (
    Plan,
    PlanItem,
)


class PlanItemInline(admin.TabularInline):
    extra = 0
    model = PlanItem


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'field',
        'agriculture',
        'seed',
        'coefficient',
        'created',
        'updated',
    )
    inlines = (PlanItemInline,)


@admin.register(PlanItem)
class PlanItemAdmin(admin.ModelAdmin):
    pass
