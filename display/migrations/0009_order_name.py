# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0008_auto_20180226_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='string', max_length=30),
        ),
    ]
