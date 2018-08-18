# Generated by Django 2.1 on 2018-08-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=100, verbose_name='Краткое название')),
                ('full_name', models.CharField(max_length=100, verbose_name='Полное название')),
            ],
            options={
                'verbose_name': 'Компания',
            },
        ),
    ]
