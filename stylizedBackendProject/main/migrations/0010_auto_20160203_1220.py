# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-03 06:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20160125_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='style',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stylesalon',
            name='num_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stylesalon',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=6),
        ),
        migrations.AddField(
            model_name='transaction',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 6, 50, 8, 645569, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=6),
        ),
    ]
