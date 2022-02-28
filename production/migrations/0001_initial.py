# Generated by Django 4.0.1 on 2022-02-28 14:57

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'w trakcie'), (1, 'zakończone')], default=0)),
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
            name='ProductionComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('productionMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='production.productionmaterial')),
            ],
        ),
    ]
