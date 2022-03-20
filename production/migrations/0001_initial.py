# Generated by Django 4.0.1 on 2022-03-19 18:54

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[('zmień status', 'zmień status'), (0, 'Przygotowywanie'), (1, 'Oczekuję'), (2, 'W trakcie'), (3, 'Zakończone')], default=2)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.DecimalField(decimal_places=4, default=Decimal('0.000'), max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.material')),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.production')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('units', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'usługa',
                'verbose_name_plural': 'usługi',
            },
        ),
        migrations.CreateModel(
            name='ProductionStockIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('length', order.models.IntegerRangeField()),
                ('width', order.models.IntegerRangeField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.material')),
                ('productionMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.productionmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('length', order.models.IntegerRangeField()),
                ('width', order.models.IntegerRangeField()),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.material')),
                ('productionMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='production.productionmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Przygotowywanie'), (1, 'Oczekuję'), (2, 'W trakcie'), (3, 'Zakończone')], default=0)),
                ('settlement', models.BooleanField(default=False)),
                ('attachments', models.FileField(upload_to='order/attachment/')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('productionMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='production.productionmaterial')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.DecimalField(decimal_places=3, default=Decimal('0.000'), max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.material')),
                ('productionorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.productionorder')),
                ('services', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='production.services')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.productionorder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='production/order/attachments/')),
                ('production_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.productionorder')),
            ],
        ),
    ]
