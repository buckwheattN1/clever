# Generated by Django 4.0.1 on 2022-04-07 14:48

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
