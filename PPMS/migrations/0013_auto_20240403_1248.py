# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-04-03 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PPMS', '0012_auto_20240330_0927'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='booking',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='booking',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
