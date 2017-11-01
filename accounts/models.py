# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    """
    user:
    date_of_birth:
    image_width:
    image_height:
    profile_image:
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    image_width = 200
    image_height = 200
    profile_image = models.ImageField(upload_to='users/profile_images/%d/%m/%Y', height_field='image_height', width_field='image_width', blank=True)
    about_me = models.TextField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return 'Profile for user {}'.format(self.user.username)
