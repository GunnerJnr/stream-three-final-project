# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class GamersHubProducts(models.Model):
    length=255
    image_width = 200
    image_height = 200

    product_images = models.ImageField(upload_to='gamershub/product_images/%d/%m/%Y', height_field='image_height', width_field='image_width', blank=True)
    name = models.CharField(max_length=length, ${blank=True, null=True} default='')
    description = models.TextField()
    price = models.DecimalField(max digits=6, decimal places=2)