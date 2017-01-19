# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0006_auto_20170118_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancerecord',
            name='Absent_Students',
        ),
        migrations.AlterField(
            model_name='attendancerecord',
            name='Present_Students',
            field=models.ManyToManyField(related_name='Attendance_Records', to='prof.Student'),
        ),
    ]
