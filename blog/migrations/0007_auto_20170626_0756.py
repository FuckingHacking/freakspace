# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postviews',
            name='post',
        ),
        migrations.DeleteModel(
            name='PostViews',
        ),
    ]
