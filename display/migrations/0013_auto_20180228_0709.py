# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-28 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0012_auto_20180226_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank='True', null='True', upload_to='photos/'),
        ),
    ]
