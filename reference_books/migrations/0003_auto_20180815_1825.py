# Generated by Django 2.1 on 2018-08-15 18:25

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0002_auto_20180815_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='polygon',
            field=django.contrib.gis.db.models.fields.PolygonField(geography=True, srid=4326, verbose_name='Полигон поля'),
        ),
    ]
