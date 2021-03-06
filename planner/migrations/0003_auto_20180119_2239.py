# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-19 22:39
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20171208_0450_squashed_0003_auto_20180110_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telemetrymetadata',
            name='processor',
            field=models.IntegerField(choices=[(0, 'unknown'), (3, 'bin'), (4, 'ddlog'), (1, 'ulog'), (2, 'tlog')], default=0, verbose_name='telemetry parser'),
        ),
    ]
