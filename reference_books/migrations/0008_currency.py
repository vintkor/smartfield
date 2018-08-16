# Generated by Django 2.1 on 2018-08-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0007_fertilizer_protection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('iso_4217_letter_code', models.CharField(max_length=3, verbose_name='ISO 4217 символьный код')),
                ('iso_4217_numeric_code', models.PositiveSmallIntegerField(max_length=3, verbose_name='ISO 4217 цыфровой код')),
                ('short_symbol', models.CharField(blank=True, max_length=5, null=True, verbose_name='Символ')),
                ('short_name', models.CharField(blank=True, max_length=5, null=True, verbose_name='Аббревиатура')),
                ('is_main', models.BooleanField(default=False, verbose_name='Является основной')),
            ],
            options={
                'verbose_name': 'Валюта',
                'verbose_name_plural': 'Валюты',
            },
        ),
    ]
