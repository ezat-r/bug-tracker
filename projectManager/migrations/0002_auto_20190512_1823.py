# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-12 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issueproject',
            name='projectName',
            field=models.CharField(max_length=30),
        ),
    ]