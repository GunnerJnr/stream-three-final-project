# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
