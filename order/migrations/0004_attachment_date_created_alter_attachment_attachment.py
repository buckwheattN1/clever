# Generated by Django 4.0.1 on 2022-01-28 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_attachment_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
