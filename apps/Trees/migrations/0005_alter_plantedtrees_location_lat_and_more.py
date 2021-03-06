# Generated by Django 4.0.2 on 2022-02-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trees', '0004_alter_plantedtrees_planted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantedtrees',
            name='location_lat',
            field=models.DecimalField(blank=True, decimal_places=22, max_digits=22, null=True, verbose_name='Lat'),
        ),
        migrations.AlterField(
            model_name='plantedtrees',
            name='location_long',
            field=models.DecimalField(blank=True, decimal_places=22, max_digits=22, null=True, verbose_name='Long'),
        ),
    ]
