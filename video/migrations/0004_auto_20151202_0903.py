# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-02 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20151202_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Series'),
        ),
    ]
