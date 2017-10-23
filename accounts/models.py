# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    """
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    image_width = 200
    image_height = 200
    profile_image = models.ImageField(upload_to='users/profile_images/%d/%m/%Y', height_field='image_height', width_field='image_width', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
