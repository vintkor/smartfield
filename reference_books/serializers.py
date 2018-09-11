from rest_framework.serializers import ModelSerializer
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


class CurrencySerializer(ModelSerializer):
    """Сериализация валюты"""

    class Meta:
        model = Currency
        fields = (
            "id",
            "title",
            "iso_4217_letter_code",
            "iso_4217_numeric_code",
            "short_symbol",
            "is_main",
        )


class UnitSerializer(ModelSerializer):
    """Сериализация Единицы измерения"""

    class Meta:
        model = Unit
        fields = (
            "id",
            "short_name",
            "long_name",
        )
