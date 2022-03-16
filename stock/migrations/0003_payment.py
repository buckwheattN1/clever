# Generated by Django 4.0.1 on 2022-03-16 07:55

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_grnmaterial_price_gross_grnmaterial_price_net_unit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('IW_IY', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Niesprawdzony'), (1, 'Sprawdzony')], default=0)),
                ('cash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.cash')),
            ],
        ),
    ]
