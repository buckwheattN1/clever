# Generated by Django 4.0.1 on 2022-02-07 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_remove_formatka_karta_remove_production_stocks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='stocks',
            field=models.ManyToManyField(blank=True, to='stock.Stock'),
        ),
    ]
