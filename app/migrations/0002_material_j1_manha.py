# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='j1_manha',
            field=models.CharField(default='-', max_length=300),
        ),
    ]
