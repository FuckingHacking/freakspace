# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20170705_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='last_activity',
        ),
    ]
