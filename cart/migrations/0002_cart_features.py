# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-22 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_features_status'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='features',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='features.Features'),
        ),
    ]
