# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-03-30 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PPMS', '0011_booking_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
