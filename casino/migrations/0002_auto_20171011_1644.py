# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-11 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='fecha_emision',
            field=models.DateField(null=True),
        ),
    ]
