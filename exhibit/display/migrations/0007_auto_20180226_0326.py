# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0006_auto_20180226_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.Category'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='display.Location'),
        ),
    ]
