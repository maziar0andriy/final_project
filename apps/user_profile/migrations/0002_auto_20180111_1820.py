# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-11 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=12, unique=True, verbose_name='Номер телефону'),
        ),
    ]
