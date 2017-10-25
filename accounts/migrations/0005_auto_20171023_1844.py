# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20171023_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, height_field='image_height', upload_to='users/profile_images/%d/%m/%Y', width_field='image_width'),
        ),
    ]