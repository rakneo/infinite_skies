# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfiniteSkiesAPI', '0002_auto_20161228_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='copyright',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
