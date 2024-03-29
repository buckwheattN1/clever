# Generated by Django 4.0.1 on 2022-04-12 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_remove_stock_warehouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('content', models.TextField()),
                ('grn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.goodsreceivednote')),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='grn/attachments/')),
                ('grn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.goodsreceivednote')),
            ],
        ),
    ]
