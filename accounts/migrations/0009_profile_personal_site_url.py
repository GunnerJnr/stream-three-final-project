# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20171102_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='personal_site_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]