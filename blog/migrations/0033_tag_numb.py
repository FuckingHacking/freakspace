# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_remove_playlist_author_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='numb',
            field=models.IntegerField(default=0),
        ),
    ]
