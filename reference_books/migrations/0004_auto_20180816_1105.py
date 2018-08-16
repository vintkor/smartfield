# Generated by Django 2.1 on 2018-08-16 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0003_auto_20180815_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmingTechniques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='reference_books')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Самоходная техника',
                'verbose_name_plural': 'Самоходная техника',
            },
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Топливо',
                'verbose_name_plural': 'Топливо',
            },
        ),
        migrations.CreateModel(
            name='Machinery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='reference_books')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('farming_techniques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_books.FarmingTechniques', verbose_name='Самоходная техника')),
            ],
            options={
                'verbose_name': 'Прицепной аггрегат',
                'verbose_name_plural': 'Прицепные аггрегаты',
            },
        ),
        migrations.CreateModel(
            name='WorkAndTechnique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_rate', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Расход топлива')),
                ('farming_techniques', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_books.FarmingTechniques', verbose_name='Самоходная техника')),
                ('fuel_rate_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_books.Unit', verbose_name='Ед. измерения расхода топлива')),
                ('machinery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reference_books.Machinery', verbose_name='Прицепной аггрегат')),
            ],
            options={
                'verbose_name': 'Работа и техника',
                'verbose_name_plural': 'Работа и техника',
            },
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Вид работ',
                'verbose_name_plural': 'Виды работ',
            },
        ),
        migrations.AddField(
            model_name='workandtechnique',
            name='work_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_books.WorkType', verbose_name='Вид работ'),
        ),
    ]
