# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 01:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prof', '0009_auto_20170119_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
