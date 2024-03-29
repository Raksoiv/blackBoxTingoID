# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-11 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casino', '0002_auto_20171011_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='tipo',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='ticket',
            name='valor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='valido',
            field=models.BooleanField(default=True),
        ),
    ]
