# Generated by Django 4.0.1 on 2022-01-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='name',
            field=models.CharField(default='magazyn', max_length=255),
        ),
    ]
