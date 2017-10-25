# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 21:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamersblog', '0007_blogpost_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_images',
            field=models.ImageField(blank=True, height_field='image_height', upload_to='users/blog_post_images/%d/%m/%Y', width_field='image_width'),
        ),
    ]
