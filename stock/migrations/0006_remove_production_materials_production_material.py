# Generated by Django 4.0.1 on 2022-02-06 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('stock', '0005_rename_reducematerial_production_materialused'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='production',
            name='materials',
        ),
        migrations.AddField(
            model_name='production',
            name='material',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.material'),
            preserve_default=False,
        ),
    ]
