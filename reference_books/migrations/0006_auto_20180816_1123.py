# Generated by Django 2.1 on 2018-08-16 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0005_auto_20180816_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ('long_name',), 'verbose_name': 'Единица измерения', 'verbose_name_plural': 'Единицы измерения'},
        ),
    ]