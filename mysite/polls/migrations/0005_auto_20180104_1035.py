# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-04 02:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180104_0909'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='username',
            new_name='User',
        ),
    ]
