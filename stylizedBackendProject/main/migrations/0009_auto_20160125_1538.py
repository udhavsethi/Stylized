# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160112_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstylesalon',
            name='style_salon',
        ),
        migrations.RemoveField(
            model_name='userstylesalon',
            name='user',
        ),
        migrations.AddField(
            model_name='transaction',
            name='user_rating',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='history',
            field=models.ManyToManyField(through='main.Transaction', to='main.StyleSalon'),
        ),
        migrations.DeleteModel(
            name='UserStyleSalon',
        ),
    ]