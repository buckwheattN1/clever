# Generated by Django 4.0.1 on 2022-03-30 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offer', '0009_offeritem_delete_offeritems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offeritem',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offer.offer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]