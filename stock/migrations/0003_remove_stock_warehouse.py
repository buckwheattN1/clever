# Generated by Django 4.0.1 on 2022-04-06 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_gender_material_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='warehouse',
        ),
    ]
