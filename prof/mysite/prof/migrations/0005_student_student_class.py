# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0004_auto_20170118_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Student_Class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prof.Class'),
        ),
    ]