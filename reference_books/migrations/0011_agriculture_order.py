# Generated by Django 2.1 on 2018-09-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0010_auto_20180906_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='agriculture',
            name='order',
            field=models.PositiveSmallIntegerField(default=100, verbose_name='Рекоммендуемый порядок посева'),
        ),
    ]