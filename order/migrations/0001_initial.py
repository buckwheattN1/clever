# Generated by Django 4.0.1 on 2022-01-26 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import order.models
import randomslugfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Milling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'frez',
                'verbose_name_plural': 'frezy',
            },
        ),
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'wzór',
                'verbose_name_plural': 'wzory',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', randomslugfield.fields.RandomSlugField(blank=True, editable=False, exclude_lower=True, exclude_upper=True, exclude_vowels=True, length=7, max_length=7, unique=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Oczekuję'), (1, 'W trakcie'), (2, 'Zakończone')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'zamówienie',
                'verbose_name_plural': 'zamówienia',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.CharField(blank=True, max_length=255, null=True)),
                ('length', models.DecimalField(decimal_places=0, max_digits=4)),
                ('width', models.DecimalField(decimal_places=0, max_digits=4)),
                ('quantity', models.SmallIntegerField(default=1)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('length1', order.models.CustomBooleanField()),
                ('length2', order.models.CustomBooleanField()),
                ('width1', order.models.CustomBooleanField()),
                ('width2', order.models.CustomBooleanField()),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order')),
            ],
            options={
                'verbose_name': 'formatka',
                'verbose_name_plural': 'formatki',
            },
        ),
    ]
