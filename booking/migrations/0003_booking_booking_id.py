# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-22 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20180722_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_id',
            field=models.CharField(default=uuid.UUID('69d9638d-32fe-454a-94ba-42bd93e43275'), max_length=254),
        ),
    ]