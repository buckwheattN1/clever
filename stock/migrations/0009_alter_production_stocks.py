# Generated by Django 4.0.1 on 2022-02-06 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_alter_production_material_alter_production_stocks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='stocks',
            field=models.ManyToManyField(blank=True, to='stock.Stock'),
        ),
    ]