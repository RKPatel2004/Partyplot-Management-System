# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-03-29 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PPMS', '0010_auto_20240329_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='venue',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='PPMS.Venue'),
        ),
    ]
