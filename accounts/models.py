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
    about_me = models.TextField(max_length=500, blank=True, null=True)
    fave_game = models.CharField(max_length=50, blank=True, null=True)
    facebook_url = models.URLField(max_length=200, blank=True, null=True)
    github_url = models.URLField(max_length=200, blank=True, null=True)
    twitter_url = models.URLField(max_length=200, blank=True, null=True)
    google_plus_url = models.URLField(max_length=200, blank=True, null=True)
    youtube_url = models.URLField(max_length=200, blank=True, null=True)
    personal_site_url = models.URLField(max_length=200, blank=True, null=True)


    def about_me_description(self):
        return self.about_me
    about_me_description.short_description = "The users about me entry"
    about_me_desc = property(about_me_description)


    def __unicode__(self):
        return 'Profile for user {}'.format(self.user.username)