# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-03 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cli', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
