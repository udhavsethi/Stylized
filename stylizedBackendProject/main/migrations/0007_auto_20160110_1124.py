# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160107_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(related_name='_user_bookmarks_+', to='main.Style'),
        ),
        migrations.AlterField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(related_name='_user_likes_+', to='main.Style'),
        ),
    ]
