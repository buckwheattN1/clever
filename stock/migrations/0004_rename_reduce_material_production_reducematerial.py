# Generated by Django 4.0.1 on 2022-02-06 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_production_reduce_material_alter_stock_material'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='reduce_material',
            new_name='reduceMaterial',
        ),
    ]
