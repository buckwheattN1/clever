# Generated by Django 4.0.1 on 2022-03-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0011_remove_materialservices_transport_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='status',
            field=models.SmallIntegerField(choices=[('zmień status', 'zmień status'), (0, 'Przygotowywanie'), (1, 'Oczekuję'), (2, 'W trakcie'), (3, 'Zakończone')], default=2),
        ),
    ]