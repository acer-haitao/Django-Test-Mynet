# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-24 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job51', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job51',
            name='jobaddress',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
