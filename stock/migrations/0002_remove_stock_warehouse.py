# Generated by Django 4.0.1 on 2022-03-23 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='warehouse',
        ),
    ]