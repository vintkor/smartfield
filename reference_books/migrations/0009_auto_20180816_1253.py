# Generated by Django 2.1 on 2018-08-16 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0008_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='iso_4217_numeric_code',
            field=models.PositiveSmallIntegerField(verbose_name='ISO 4217 цыфровой код'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='short_symbol',
            field=models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.MaxLengthValidator(limit_value=3)], verbose_name='Символ'),
        ),
    ]
