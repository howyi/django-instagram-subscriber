# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='testchar',
        ),
        migrations.AddField(
            model_name='media',
            name='data',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
