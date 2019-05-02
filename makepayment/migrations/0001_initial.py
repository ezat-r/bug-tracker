# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-02 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bugDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=50)),
                ('streetAddress1', models.CharField(max_length=40)),
                ('streetAddress2', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('postCode', models.CharField(max_length=20)),
                ('paymentDate', models.DateTimeField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugDB.Issue')),
            ],
        ),
    ]
