import decimal

from django.test import TestCase
from .models import (
    Fuel,
    FuelCoast,
)


class FuelModelTest(TestCase):
    def setUp(self):
        Fuel.objects.create(
            title='test fuel'
        )

    def test_save_model(self):
        saved_models = Fuel.objects.count()
        self.assertEqual(saved_models, 1)

    def test_str_method(self):
        fuel_obj = Fuel.objects.first()
        self.assertEqual(str(fuel_obj), fuel_obj.title)


class FuelCoastModelTest(TestCase):
    def setUp(self):
        fuel = Fuel.objects.create(
            title='test fuel'
        )
        FuelCoast.objects.create(
            fuel=fuel,
            price=decimal.Decimal(12.32)
        )

    def test_save_model(self):
        saved_models = FuelCoast.objects.count()
        self.assertEqual(saved_models, 1)

    def test_parent_title(self):
        title = FuelCoast.objects.first().fuel.title
        self.assertEqual(title, 'test fuel')
