# Generated by Django 4.0.1 on 2022-04-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_customer_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='nip',
            field=models.PositiveIntegerField(blank=True, default=1234567890),
            preserve_default=False,
        ),
    ]
