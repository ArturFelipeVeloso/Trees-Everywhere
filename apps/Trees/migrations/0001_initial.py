# Generated by Django 4.0.2 on 2022-02-21 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('scientific_name', models.CharField(max_length=200, verbose_name='Scientific Name')),
            ],
            options={
                'verbose_name': 'Tree',
                'verbose_name_plural': 'Trees',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='PlantedTrees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('planted_at', models.DateTimeField(verbose_name='Planted at')),
                ('about', models.TextField(blank=True)),
                ('location_long', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('location_lat', models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True)),
                ('tree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Trees.plant', verbose_name='Plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Planted Tree',
                'verbose_name_plural': 'Planted Trees',
                'ordering': ('pk',),
            },
        ),
    ]
