# Generated by Django 2.0.5 on 2018-05-23 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_quote', '0005_auto_20180523_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclequote',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='vehiclequote',
            name='list_price',
        ),
        migrations.AddField(
            model_name='vehiclequote',
            name='quoted_price',
            field=models.FloatField(null=True),
        ),
    ]
