# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-23 17:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0005_waypoint_altitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +9999999999. 10 to 15 digits allowed.', regex='^\\+\\d{10,15}$')], verbose_name='mobile phone number'),
        ),
    ]