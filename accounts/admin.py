"""
Admin.py:
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Profile


# Create Our Admin Model for User Details
class ProfileAdmin(admin.ModelAdmin):
    """
    ProfileAdmin(admin.ModelAdmin):
        The user details we wish to display in the admin panel
    """
    list_display = [
        'user',
        'date_of_birth',
        ]


admin.site.register(Profile, ProfileAdmin)
