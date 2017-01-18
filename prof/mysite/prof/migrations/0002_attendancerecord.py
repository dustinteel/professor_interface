# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Associated_Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prof.Class')),
            ],
        ),
    ]
