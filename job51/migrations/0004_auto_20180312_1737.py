# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-12 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job51', '0003_auto_20180312_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job51',
            name='jobtxt',
            field=models.TextField(),
        ),
    ]
