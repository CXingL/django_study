# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pud_date',
            new_name='pub_date',
        ),
    ]
