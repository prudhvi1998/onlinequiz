# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_answer_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Score',
            field=models.IntegerField(default=0),
        ),
    ]
