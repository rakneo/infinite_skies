# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-28 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfiniteSkiesAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='hdurl',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='data',
            name='media_type',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='data',
            name='service_ver',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='data',
            name='url',
            field=models.CharField(max_length=1500),
        ),
    ]
