# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-22 18:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='features',
        ),
    ]