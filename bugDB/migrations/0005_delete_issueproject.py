# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-12 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugDB', '0004_auto_20190506_1230'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IssueProject',
        ),
    ]
