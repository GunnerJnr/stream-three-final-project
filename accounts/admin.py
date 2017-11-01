# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from accounts.models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'about_me', 'fave_game', 'profile_image']


admin.site.register(Profile, ProfileAdmin)
