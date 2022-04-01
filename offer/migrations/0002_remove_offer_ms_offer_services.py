# Generated by Django 4.0.1 on 2022-03-29 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0007_productionorder_description'),
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='ms',
        ),
        migrations.AddField(
            model_name='offer',
            name='services',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='production.services'),
            preserve_default=False,
        ),
    ]