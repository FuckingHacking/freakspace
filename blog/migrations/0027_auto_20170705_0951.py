# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_userprofile_last_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatar'),
        ),
    ]
