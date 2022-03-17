# Generated by Django 4.0.1 on 2022-03-17 12:59

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import order.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nip', models.CharField(max_length=13)),
                ('regon', models.CharField(blank=True, max_length=13)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('fax', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
            ],
            options={
                'verbose_name': 'Kontrahent',
                'verbose_name_plural': 'Kontrahenci',
            },
        ),
        migrations.CreateModel(
            name='Cutter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(null=True)),
                ('toBuy', models.IntegerField(blank=True, default=0, null=True)),
                ('forSharpening', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsReceivedNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('documentID', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Niezatwierdzone'), (1, 'Zatwierdzone')], default=0)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.contractor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', order.models.IntegerRangeField(null=True)),
                ('width', order.models.IntegerRangeField(null=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='order.material')),
            ],
        ),
        migrations.CreateModel(
            name='GRNMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.DecimalField(decimal_places=4, default=Decimal('0.000'), max_digits=10)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price_net_unit', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('price_net', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('price_gross', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('vat', models.SmallIntegerField(choices=[(0, '8%'), (1, '23%')], default=1)),
                ('vat_amount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('grn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.goodsreceivednote')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.material')),
            ],
        ),
    ]
