# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160103_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='style',
            old_name='style_cat',
            new_name='category',
        ),
    ]
