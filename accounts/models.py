"""
Models.py:
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


# Create our class to handle the user profile
class Profile(models.Model):
    """
    user: create the user model
    date_of_birth: the users date of birth
    image_width: the width of the profile image
    image_height: the height of the profile image
    profile_image:the profile image model
    about_me: about me text field
    fave_game: the users fave game text field
    facebook_url: the users facebook url
    github_url: the users github url
    twitter_url: the users twitter url
    google_plus_url: the users google plus url
    youtube_url: the users youtube url
    personal_site_url: the users personal website url
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    image_width = 200
    image_height = 200
    profile_image = models.ImageField(
        upload_to='users/profile_images/%d/%m/%Y',
        height_field='image_height',
        width_field='image_width',
        blank=True
        )
    about_me = models.TextField(max_length=500, blank=True, null=True)
    fave_game = models.CharField(max_length=50, blank=True, null=True)
    facebook_url = models.URLField(max_length=200, blank=True, null=True)
    github_url = models.URLField(max_length=200, blank=True, null=True)
    twitter_url = models.URLField(max_length=200, blank=True, null=True)
    google_plus_url = models.URLField(max_length=200, blank=True, null=True)
    youtube_url = models.URLField(max_length=200, blank=True, null=True)
    personal_site_url = models.URLField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return 'Profile for user {}'.format(self.user)

    # define a view to handle the users about section
    def about_me_description(self):
        """
        about_me_description(self):
        """
        return self.about_me

    # display a more readable description in the admin panel
    about_me_description.short_description = "The users about me entry"
    about_me_desc = property(about_me_description)
